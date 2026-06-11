from __future__ import annotations
import os
import threading
import datetime
import customtkinter as ctk
from tkinter import filedialog, messagebox
from typing import TYPE_CHECKING

from models.collection_manager import (
    obtener_resumen_global,
    obtener_faltantes,
    obtener_repetidas,
)
from models.exporter import exportar_faltantes_docx, exportar_repetidas_docx

if TYPE_CHECKING:
    from views.main_window import MainWindow

VERDE_OSCURO  = ("#1A4731", "#0F2E20")
VERDE_MEDIO   = ("#236040", "#1A4731")
VERDE_CLARO   = ("#E8F5EE", "#1E3A2A")
DORADO        = ("#F5C842", "#F5C842")
DORADO_HOVER  = ("#D4A830", "#D4A830")
BG_MAIN       = ("#F4F6F3", "#1C1C1E")
BG_CARD       = ("#FFFFFF", "#2C2C2E")
TEXTO_PRI     = ("#1C1C1E", "#F5F5F5")
TEXTO_SEC     = ("#555555", "#AAAAAA")
BORDE         = ("#D0D0D0", "#3A3A3C")
VERDE_BTN     = ("#2E7D52", "#3A9E6A")
VERDE_BTN_HOV = ("#1A5C3A", "#2E8055")
AZUL_BTN      = ("#1A3A6C", "#2A5298")
AZUL_HOV      = ("#122A52", "#1E3D7A")
OK_COLOR      = ("#1A7A3A", "#2ECC71")
ERR_COLOR     = ("#CC2222", "#FF5555")


class ExportView(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, main_window: "MainWindow") -> None:
        super().__init__(parent, fg_color=BG_MAIN, corner_radius=0)
        self.main_window = main_window

        self._n_faltantes: int = 0
        self._n_repetidas: int = 0
        self._cod_pais_filtro: str | None = None  
        self._log_entries: list[ctk.CTkLabel] = []

        self._build()
        self.refresh()

    def _build(self) -> None:
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._build_header()
        self._build_export_cards()
        self._build_filter_bar()
        self._build_log()

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, padx=24, pady=(20, 4), sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header,
            text="Exportar reportes",
            font=ctk.CTkFont(family="Arial", size=26, weight="bold"),
            text_color=TEXTO_PRI,
            anchor="w",
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            header,
            text="Genera archivos Word (.docx) con el listado de figuritas faltantes o repetidas.",
            font=ctk.CTkFont(size=13),
            text_color=TEXTO_SEC,
            anchor="w",
        ).grid(row=1, column=0, sticky="w")

    def _build_export_cards(self) -> None:
        cards_row = ctk.CTkFrame(self, fg_color="transparent")
        cards_row.grid(row=1, column=0, padx=24, pady=(12, 8), sticky="ew")
        cards_row.grid_columnconfigure((0, 1), weight=1)

        self._card_faltantes = _ExportCard(
            cards_row,
            titulo="📋  Figuritas faltantes",
            descripcion="Lista todas las figuritas que aún no tienes.",
            color_acento=VERDE_BTN,
            color_hover=VERDE_BTN_HOV,
            on_export=self._exportar_faltantes,
        )
        self._card_faltantes.grid(row=0, column=0, padx=(0, 8), sticky="nsew")

        self._card_repetidas = _ExportCard(
            cards_row,
            titulo="🔁  Figuritas repetidas",
            descripcion="Lista las figuritas extra disponibles para intercambio.",
            color_acento=AZUL_BTN,
            color_hover=AZUL_HOV,
            on_export=self._exportar_repetidas,
        )
        self._card_repetidas.grid(row=0, column=1, padx=(8, 0), sticky="nsew")

    def _build_filter_bar(self) -> None:
        bar = ctk.CTkFrame(
            self, fg_color=BG_CARD, corner_radius=12,
            border_width=1, border_color=BORDE,
        )
        bar.grid(row=2, column=0, padx=24, pady=(0, 12), sticky="ew")
        bar.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            bar,
            text="🌍  Filtrar por país:",
            font=ctk.CTkFont(size=13),
            text_color=TEXTO_SEC,
        ).grid(row=0, column=0, padx=(16, 8), pady=12, sticky="w")

        from models.collection_manager import obtener_todos_los_paises
        try:
            paises = obtener_todos_los_paises()
        except Exception:
            paises = []

        opciones = ["Todos los países"] + [
            f"{p.cod_pais} — {p.nombre}" for p in paises
        ]

        self.combo_pais = ctk.CTkComboBox(
            bar,
            values=opciones,
            width=260,
            height=34,
            corner_radius=8,
            border_color=BORDE,
            button_color=VERDE_MEDIO,
            button_hover_color=VERDE_OSCURO,
            font=ctk.CTkFont(size=13),
            command=self._on_filtro_changed,
            state="readonly",
        )
        self.combo_pais.set("Todos los países")
        self.combo_pais.grid(row=0, column=1, padx=(0, 16), pady=12, sticky="w")

        ctk.CTkLabel(
            bar,
            text="Al seleccionar un país, solo se exportarán sus figuritas.",
            font=ctk.CTkFont(size=11),
            text_color=TEXTO_SEC,
        ).grid(row=0, column=2, padx=(0, 16), pady=12, sticky="e")

    def _build_log(self) -> None:
        log_frame = ctk.CTkFrame(self, fg_color="transparent")
        log_frame.grid(row=3, column=0, padx=24, pady=(0, 16), sticky="nsew")
        log_frame.grid_rowconfigure(1, weight=1)
        log_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            log_frame,
            text="Historial de exportaciones (sesión actual)",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=TEXTO_SEC,
            anchor="w",
        ).grid(row=0, column=0, pady=(0, 6), sticky="w")

        self.log_scroll = ctk.CTkScrollableFrame(
            log_frame,
            fg_color=BG_CARD,
            corner_radius=10,
            border_width=1,
            border_color=BORDE,
            scrollbar_button_color=VERDE_MEDIO,
            scrollbar_button_hover_color=DORADO,
        )
        self.log_scroll.grid(row=1, column=0, sticky="nsew")
        self.log_scroll.grid_columnconfigure(0, weight=1)

        self.lbl_log_vacio = ctk.CTkLabel(
            self.log_scroll,
            text="Aún no se han generado exportaciones en esta sesión.",
            font=ctk.CTkFont(size=12),
            text_color=TEXTO_SEC,
        )
        self.lbl_log_vacio.grid(row=0, column=0, pady=20)

    def refresh(self) -> None:
        try:
            pais = self._cod_pais_filtro
            faltantes = obtener_faltantes(pais)
            repetidas = obtener_repetidas(pais)
            self._n_faltantes = len(faltantes)
            self._n_repetidas = sum(r["disponibles"] for r in repetidas)
            n_equipos_rep = len(set(r["cod_pais"] for r in repetidas))
        except Exception:
            self._n_faltantes = 0
            self._n_repetidas = 0
            n_equipos_rep = 0

        sufijo = f" en {self._nombre_filtro()}" if self._cod_pais_filtro else ""

        self._card_faltantes.actualizar_conteo(
            conteo=self._n_faltantes,
            subtexto=f"figuritas por conseguir{sufijo}",
        )
        self._card_repetidas.actualizar_conteo(
            conteo=self._n_repetidas,
            subtexto=f"copias para intercambio{sufijo} · {n_equipos_rep} equipos",
        )

    def _on_filtro_changed(self, seleccion: str) -> None:
        if seleccion == "Todos los países":
            self._cod_pais_filtro = None
        else:
            self._cod_pais_filtro = seleccion.split("—")[0].strip()
        self.refresh()

    def _nombre_filtro(self) -> str:
        sel = self.combo_pais.get()
        if "—" in sel:
            return sel.split("—")[1].strip()
        return sel

    def _exportar_faltantes(self) -> None:
        if self._n_faltantes == 0:
            messagebox.showinfo(
                "Sin faltantes",
                "¡No tienes figuritas faltantes! El álbum está completo.",
            )
            return

        nombre_sugerido = self._nombre_archivo("faltantes")
        ruta = filedialog.asksaveasfilename(
            title="Guardar reporte de faltantes",
            defaultextension=".docx",
            filetypes=[("Documento Word", "*.docx"), ("Todos los archivos", "*.*")],
            initialfile=nombre_sugerido,
        )
        if not ruta:
            return  

        self._card_faltantes.set_cargando(True)
        threading.Thread(
            target=self._run_export,
            args=(exportar_faltantes_docx, ruta, "faltantes"),
            daemon=True,
        ).start()

    def _exportar_repetidas(self) -> None:
        if self._n_repetidas == 0:
            messagebox.showinfo(
                "Sin repetidas",
                "No tienes figuritas repetidas para intercambio.",
            )
            return

        nombre_sugerido = self._nombre_archivo("repetidas")
        ruta = filedialog.asksaveasfilename(
            title="Guardar reporte de repetidas",
            defaultextension=".docx",
            filetypes=[("Documento Word", "*.docx"), ("Todos los archivos", "*.*")],
            initialfile=nombre_sugerido,
        )
        if not ruta:
            return

        self._card_repetidas.set_cargando(True)
        threading.Thread(
            target=self._run_export,
            args=(exportar_repetidas_docx, ruta, "repetidas"),
            daemon=True,
        ).start()

    def _run_export(self, fn, ruta: str, tipo: str) -> None:
        try:
            fn(ruta_salida=ruta)
            self.after(0, lambda: self._on_export_ok(ruta, tipo))
        except Exception as e:
            self.after(0, lambda err=str(e): self._on_export_error(err, tipo))

    def _on_export_ok(self, ruta: str, tipo: str) -> None:
        card = self._card_faltantes if tipo == "faltantes" else self._card_repetidas
        card.set_cargando(False)

        nombre = os.path.basename(ruta)
        carpeta = os.path.dirname(ruta)
        self._agregar_log(
            f"✅  {nombre}  →  {carpeta}",
            color=OK_COLOR,
        )

        abrir = messagebox.askyesno(
            f"El archivo «{nombre}» se guardó correctamente.\n\n"
            f"¿Deseas abrir la carpeta destino?",
        )
        if abrir:
            self._abrir_carpeta(carpeta)

    def _on_export_error(self, error: str, tipo: str) -> None:
        card = self._card_faltantes if tipo == "faltantes" else self._card_repetidas
        card.set_cargando(False)
        self._agregar_log(f"❌  Error al exportar {tipo}: {error}", color=ERR_COLOR)
        messagebox.showerror("Error de exportación", f"No se pudo generar el archivo:\n{error}")

    def _agregar_log(self, texto: str, color: tuple) -> None:
        self.lbl_log_vacio.grid_remove()

        hora = datetime.datetime.now().strftime("%H:%M:%S")
        lbl = ctk.CTkLabel(
            self.log_scroll,
            text=f"[{hora}]  {texto}",
            font=ctk.CTkFont(size=12),
            text_color=color,
            anchor="w",
        )
        fila = len(self._log_entries)
        lbl.grid(row=fila, column=0, padx=12, pady=(4, 0), sticky="w")
        self._log_entries.append(lbl)

    def _nombre_archivo(self, tipo: str) -> str:
        fecha = datetime.datetime.now().strftime("%Y%m%d")
        pais  = f"_{self._cod_pais_filtro}" if self._cod_pais_filtro else ""
        return f"AlbumMind_{tipo}{pais}_{fecha}.docx"

    @staticmethod
    def _abrir_carpeta(ruta: str) -> None:
        import subprocess, sys
        try:
            if sys.platform == "win32":
                os.startfile(ruta)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", ruta])
            else:
                subprocess.Popen(["xdg-open", ruta])
        except Exception:
            pass

class _ExportCard(ctk.CTkFrame):
    def __init__(
        self,
        parent: ctk.CTkFrame,
        titulo: str,
        descripcion: str,
        color_acento: tuple,
        color_hover: tuple,
        on_export: callable,
    ) -> None:
        super().__init__(
            parent,
            fg_color=BG_CARD,
            corner_radius=14,
            border_width=1,
            border_color=BORDE,
        )
        self._color_acento = color_acento
        self._color_hover  = color_hover
        self._on_export    = on_export
        self._build(titulo, descripcion)

    def _build(self, titulo: str, descripcion: str) -> None:
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self,
            text=titulo,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=TEXTO_PRI,
            anchor="w",
        ).grid(row=0, column=0, padx=20, pady=(18, 4), sticky="w")

        ctk.CTkLabel(
            self,
            text=descripcion,
            font=ctk.CTkFont(size=12),
            text_color=TEXTO_SEC,
            anchor="w",
            wraplength=260,
        ).grid(row=1, column=0, padx=20, pady=(0, 12), sticky="w")

        self.lbl_conteo = ctk.CTkLabel(
            self,
            text="—",
            font=ctk.CTkFont(family="Arial", size=48, weight="bold"),
            text_color=self._color_acento,
            anchor="w",
        )
        self.lbl_conteo.grid(row=2, column=0, padx=20, pady=(0, 2), sticky="w")

        self.lbl_subtexto = ctk.CTkLabel(
            self,
            text="Cargando...",
            font=ctk.CTkFont(size=12),
            text_color=TEXTO_SEC,
            anchor="w",
        )
        self.lbl_subtexto.grid(row=3, column=0, padx=20, pady=(0, 16), sticky="w")

        ctk.CTkFrame(
            self, height=1, fg_color=BORDE,
        ).grid(row=4, column=0, padx=20, pady=(0, 16), sticky="ew")

        self.btn_exportar = ctk.CTkButton(
            self,
            text="📄  Exportar .docx",
            height=40,
            corner_radius=10,
            fg_color=self._color_acento,
            hover_color=self._color_hover,
            text_color=("#FFFFFF", "#FFFFFF"),
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._on_export,
        )
        self.btn_exportar.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="ew")

    def actualizar_conteo(self, conteo: int, subtexto: str) -> None:
        self.lbl_conteo.configure(text=str(conteo))
        self.lbl_subtexto.configure(text=subtexto)

    def set_cargando(self, cargando: bool) -> None:
        if cargando:
            self.btn_exportar.configure(
                text="⏳  Generando...",
                state="disabled",
                fg_color=("#888888", "#555555"),
            )
        else:
            self.btn_exportar.configure(
                text="📄  Exportar .docx",
                state="normal",
                fg_color=self._color_acento,
            )