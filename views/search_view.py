from __future__ import annotations
import customtkinter as ctk
from typing import TYPE_CHECKING

from models.collection_manager import (
    buscar_figuritas,
    agregar_figurita,
    quitar_figurita,
    marcar_pegada,
    obtener_item_coleccion,
)

if TYPE_CHECKING:
    from views.main_window import MainWindow

VERDE_OSCURO  = ("#1A4731", "#0F2E20")
VERDE_MEDIO   = ("#236040", "#1A4731")
VERDE_CLARO   = ("#E8F5EE", "#1E3A2A")
DORADO        = ("#F5C842", "#F5C842")
DORADO_HOVER  = ("#D4A830", "#D4A830")
BG_MAIN       = ("#F4F6F3", "#1C1C1E")
BG_CARD       = ("#FFFFFF", "#2C2C2E")
BG_ROW_PAR    = ("#FFFFFF", "#2C2C2E")
BG_ROW_IMPAR  = ("#F7FAF8", "#252525")
BG_ROW_HOV    = ("#E8F5EE", "#1E3A2A")
TEXTO_PRI     = ("#1C1C1E", "#F5F5F5")
TEXTO_SEC     = ("#555555", "#AAAAAA")
TEXTO_HEADER  = ("#FFFFFF", "#FFFFFF")
BORDE         = ("#D0D0D0", "#3A3A3C")
ROJO          = ("#CC2222", "#FF5555")
ROJO_HOVER    = ("#AA1111", "#DD3333")
VERDE_BTN     = ("#2E7D52", "#3A9E6A")
VERDE_BTN_HOV = ("#1A5C3A", "#2E8055")

COL_NUM    = 52
COL_PAIS   = 130
COL_NOMBRE = 220
COL_PAG    = 58
COL_CANT   = 56
COL_ACC    = 120
DEBOUNCE_MS = 350


class SearchView(ctk.CTkFrame):
    """Vista de búsqueda global de figuritas."""

    def __init__(self, parent: ctk.CTkFrame, main_window: "MainWindow") -> None:
        super().__init__(parent, fg_color=BG_MAIN, corner_radius=0)
        self.main_window = main_window
        self._resultados_raw: list[dict] = []
        self._filtro: str = "todos"
        self._debounce_id = None
        self._filas: list = []
        self._build()

    def _build(self) -> None:
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self._build_header()
        self._build_search_bar()
        self._build_results_header()
        self._build_table()

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, padx=24, pady=(20, 8), sticky="ew")
        ctk.CTkLabel(
            header,
            text="Buscar figuritas",
            font=ctk.CTkFont(family="Arial", size=26, weight="bold"),
            text_color=TEXTO_PRI,
            anchor="w",
        ).pack(side="left")

    def _build_search_bar(self) -> None:
        bar_outer = ctk.CTkFrame(
            self, fg_color=BG_CARD, corner_radius=12,
            border_width=1, border_color=BORDE,
        )
        bar_outer.grid(row=1, column=0, padx=24, pady=(0, 10), sticky="ew")
        bar_outer.grid_columnconfigure(0, weight=1)

        input_row = ctk.CTkFrame(bar_outer, fg_color="transparent")
        input_row.grid(row=0, column=0, padx=12, pady=(12, 6), sticky="ew")
        input_row.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            input_row, text="🔍", font=ctk.CTkFont(size=16), width=28,
        ).grid(row=0, column=0, sticky="w")

        self.entry_buscar = ctk.CTkEntry(
            input_row,
            placeholder_text="Busca por nombre, país o número de figurita...",
            height=38, corner_radius=8, border_color=BORDE,
            font=ctk.CTkFont(size=14), text_color=TEXTO_PRI,
        )
        self.entry_buscar.grid(row=0, column=0, padx=(32, 8), sticky="ew")
        self.entry_buscar.bind("<KeyRelease>", self._on_key_release)
        self.entry_buscar.bind("<Return>", lambda _e: self._ejecutar_busqueda())

        ctk.CTkButton(
            input_row, text="✕  Limpiar", width=90, height=38,
            corner_radius=8, fg_color="transparent",
            hover_color=("#EEEEEE", "#3A3A3A"),
            border_width=1, border_color=BORDE,
            text_color=TEXTO_SEC, font=ctk.CTkFont(size=13),
            command=self._limpiar,
        ).grid(row=0, column=1, sticky="e")

        filtros_row = ctk.CTkFrame(bar_outer, fg_color="transparent")
        filtros_row.grid(row=1, column=0, padx=12, pady=(0, 12), sticky="ew")

        self._filter_btns: dict[str, ctk.CTkButton] = {}
        for key, label in [("todos","Todos"), ("faltantes","❌ Solo faltantes"), ("repetidas","🔁 Repetidas")]:
            btn = ctk.CTkButton(
                filtros_row, text=label, width=130, height=28,
                corner_radius=14, border_width=1, border_color=BORDE,
                fg_color="transparent", hover_color=VERDE_CLARO,
                text_color=TEXTO_PRI, font=ctk.CTkFont(size=12),
                command=lambda k=key: self._aplicar_filtro(k),
            )
            btn.pack(side="left", padx=(0, 8))
            self._filter_btns[key] = btn
        self._marcar_filtro("todos")

    def _build_results_header(self) -> None:
        self.lbl_conteo = ctk.CTkLabel(
            self,
            text="Escribe al menos 2 caracteres para buscar.",
            font=ctk.CTkFont(size=12), text_color=TEXTO_SEC, anchor="w",
        )
        self.lbl_conteo.grid(row=2, column=0, padx=28, pady=(0, 4), sticky="w")

    def _build_table(self) -> None:
        table_outer = ctk.CTkFrame(self, fg_color="transparent")
        table_outer.grid(row=3, column=0, padx=24, pady=(0, 16), sticky="nsew")
        table_outer.grid_rowconfigure(1, weight=1)
        table_outer.grid_columnconfigure(0, weight=1)

        hdr = ctk.CTkFrame(table_outer, fg_color=VERDE_OSCURO, corner_radius=8, height=36)
        hdr.grid(row=0, column=0, sticky="ew", pady=(0, 2))
        hdr.grid_propagate(False)
        for texto, ancho, anchor in [
            ("#", COL_NUM, "center"), ("País", COL_PAIS, "w"),
            ("Jugador", COL_NOMBRE, "w"), ("Pág.", COL_PAG, "center"),
            ("Cant.", COL_CANT, "center"), ("Acciones", COL_ACC, "center"),
        ]:
            ctk.CTkLabel(
                hdr, text=texto,
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color=TEXTO_HEADER, width=ancho, anchor=anchor,
            ).pack(side="left", padx=(8, 0))

        self.scroll = ctk.CTkScrollableFrame(
            table_outer, fg_color=BG_MAIN, corner_radius=0,
            scrollbar_button_color=VERDE_MEDIO,
            scrollbar_button_hover_color=DORADO,
        )
        self.scroll.grid(row=1, column=0, sticky="nsew")
        self.scroll.grid_columnconfigure(0, weight=1)
        self._mostrar_placeholder("Usa el buscador para encontrar figuritas.")

    def _on_key_release(self, _event=None) -> None:
        if self._debounce_id is not None:
            self.after_cancel(self._debounce_id)
        self._debounce_id = self.after(DEBOUNCE_MS, self._ejecutar_busqueda)

    def _ejecutar_busqueda(self) -> None:
        termino = self.entry_buscar.get().strip()
        if len(termino) < 2:
            self._resultados_raw = []
            self.lbl_conteo.configure(text="Escribe al menos 2 caracteres para buscar.")
            self._renderizar([])
            self._mostrar_placeholder("Usa el buscador para encontrar figuritas.")
            return
        try:
            self._resultados_raw = buscar_figuritas(termino)
        except Exception as e:
            self.lbl_conteo.configure(text=f"Error: {e}")
            return
        self._aplicar_filtro(self._filtro)

    def _aplicar_filtro(self, filtro: str) -> None:
        self._filtro = filtro
        self._marcar_filtro(filtro)
        if filtro == "faltantes":
            datos = [r for r in self._resultados_raw if r["cantidad"] == 0]
        elif filtro == "repetidas":
            datos = [r for r in self._resultados_raw if r["cantidad"] > 1]
        else:
            datos = self._resultados_raw

        total    = len(self._resultados_raw)
        visibles = len(datos)
        termino  = self.entry_buscar.get().strip()
        if termino:
            sufijo = f" (mostrando {visibles})" if visibles != total else ""
            self.lbl_conteo.configure(
                text=f"{total} resultado{'s' if total != 1 else ''} para «{termino}»{sufijo}"
            )
        else:
            self.lbl_conteo.configure(text="Escribe al menos 2 caracteres para buscar.")
        self._renderizar(datos)

    def _marcar_filtro(self, activo: str) -> None:
        for key, btn in self._filter_btns.items():
            if key == activo:
                btn.configure(fg_color=VERDE_OSCURO, text_color=("#FFFFFF","#FFFFFF"),
                              border_color=VERDE_OSCURO, font=ctk.CTkFont(size=12, weight="bold"))
            else:
                btn.configure(fg_color="transparent", text_color=TEXTO_PRI,
                              border_color=BORDE, font=ctk.CTkFont(size=12, weight="normal"))

    def _renderizar(self, datos: list[dict]) -> None:
        for fila in self._filas:
            fila.destroy()
        self._filas.clear()
        if not datos:
            self._mostrar_placeholder(
                "No se encontraron figuritas." if self.entry_buscar.get().strip()
                else "Usa el buscador para encontrar figuritas."
            )
            return
        for idx, row_data in enumerate(datos):
            bg = BG_ROW_IMPAR if idx % 2 else BG_ROW_PAR
            fila = _ResultRow(
                self.scroll, data=row_data, bg=bg,
                on_change=self._on_row_changed,
                on_nav=lambda cod=row_data["cod_pais"]: self.main_window.navigate_to_country(cod),
            )
            fila.grid(row=idx, column=0, sticky="ew", pady=(0, 1))
            self._filas.append(fila)

    def _mostrar_placeholder(self, texto: str) -> None:
        ph = ctk.CTkLabel(self.scroll, text=texto,
                          font=ctk.CTkFont(size=14), text_color=TEXTO_SEC)
        ph.grid(row=0, column=0, pady=60)
        self._filas.append(ph)

    def _limpiar(self) -> None:
        self.entry_buscar.delete(0, "end")
        self._resultados_raw = []
        self._renderizar([])
        self._mostrar_placeholder("Usa el buscador para encontrar figuritas.")
        self.lbl_conteo.configure(text="Escribe al menos 2 caracteres para buscar.")

    def _on_row_changed(self, num_figura: int, cod_pais: str) -> None:
        try:
            item = obtener_item_coleccion(num_figura, cod_pais)
            for r in self._resultados_raw:
                if r["num_figura"] == num_figura and r["cod_pais"] == cod_pais:
                    r["cantidad"] = item.cantidad
                    r["pegada"]   = int(item.pegada)
                    break
        except Exception:
            pass
        self.main_window.on_collection_changed()

    def refresh(self) -> None:
        self._ejecutar_busqueda()

class _ResultRow(ctk.CTkFrame):
    """Fila de la tabla de resultados con controles inline."""

    def __init__(self, parent, data: dict, bg: tuple,
                 on_change, on_nav) -> None:
        super().__init__(parent, fg_color=bg, corner_radius=6, height=40)
        self.grid_propagate(False)
        self._data      = data
        self._bg        = bg
        self._on_change = on_change
        self._on_nav    = on_nav
        self._build()
        self._bind_hover(self)

    def _build(self) -> None:
        d        = self._data
        cantidad = d["cantidad"]
        pegada   = bool(d["pegada"])

        ctk.CTkLabel(self, text=f"#{d['num_figura']}",
                     font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=TEXTO_SEC, width=COL_NUM, anchor="center",
                     ).pack(side="left", padx=(8, 0))

        nombre_pais = d["nombre_pais"]
        if len(nombre_pais) > 14:
            nombre_pais = nombre_pais[:12] + "…"
        ctk.CTkLabel(self, text=nombre_pais, font=ctk.CTkFont(size=12),
                     text_color=TEXTO_PRI, width=COL_PAIS, anchor="w",
                     ).pack(side="left", padx=(8, 0))

        nombre = self._nombre_display(d)
        if len(nombre) > 24:
            nombre = nombre[:22] + "…"
        ctk.CTkLabel(self, text=nombre, font=ctk.CTkFont(size=12),
                     text_color=TEXTO_PRI, width=COL_NOMBRE, anchor="w",
                     ).pack(side="left", padx=(8, 0))

        ctk.CTkLabel(self, text=str(d["num_pagina"]), font=ctk.CTkFont(size=12),
                     text_color=TEXTO_SEC, width=COL_PAG, anchor="center",
                     ).pack(side="left", padx=(4, 0))

        self.lbl_cantidad = ctk.CTkLabel(
            self, text=str(cantidad),
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=VERDE_BTN if cantidad > 0 else TEXTO_SEC,
            width=COL_CANT, anchor="center",
        )
        self.lbl_cantidad.pack(side="left", padx=(4, 0))

        acc = ctk.CTkFrame(self, fg_color="transparent", width=COL_ACC)
        acc.pack(side="left", padx=(4, 8))
        acc.pack_propagate(False)

        self.btn_menos = ctk.CTkButton(
            acc, text="−", width=26, height=26, corner_radius=5,
            fg_color=ROJO if cantidad > 0 else ("#DDDDDD","#444444"),
            hover_color=ROJO_HOVER, text_color=("#FFFFFF","#FFFFFF"),
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._quitar,
            state="normal" if cantidad > 0 else "disabled",
        )
        self.btn_menos.pack(side="left", padx=(0, 2))

        self.btn_mas = ctk.CTkButton(
            acc, text="+", width=26, height=26, corner_radius=5,
            fg_color=VERDE_BTN, hover_color=VERDE_BTN_HOV,
            text_color=("#FFFFFF","#FFFFFF"),
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._agregar,
        )
        self.btn_mas.pack(side="left", padx=(0, 4))

        self.btn_pegar = ctk.CTkButton(
            acc, text="✅" if pegada else "□",
            width=26, height=26, corner_radius=5,
            fg_color=DORADO if pegada else "transparent",
            hover_color=DORADO_HOVER,
            border_width=0 if pegada else 1, border_color=BORDE,
            text_color=("#1C1C1E","#1C1C1E") if pegada else TEXTO_SEC,
            font=ctk.CTkFont(size=13),
            command=self._toggle_pegada,
            state="normal" if cantidad > 0 else "disabled",
        )
        self.btn_pegar.pack(side="left", padx=(0, 4))

        ctk.CTkButton(
            acc, text="→", width=26, height=26, corner_radius=5,
            fg_color="transparent", hover_color=VERDE_CLARO,
            border_width=1, border_color=BORDE,
            text_color=VERDE_OSCURO, font=ctk.CTkFont(size=13, weight="bold"),
            command=self._on_nav,
        ).pack(side="left")

    @staticmethod
    def _nombre_display(d: dict) -> str:
        nombre   = d.get("nombre_jugador") or ""
        apellido = d.get("apellido_jugador") or ""
        especial = d.get("tipo_especial") or ""
        completo = f"{nombre} {apellido}".strip()
        return completo if completo else (especial or "—")

    def _bind_hover(self, widget) -> None:
        widget.bind("<Enter>", lambda _e: self._hover(True))
        widget.bind("<Leave>", lambda _e: self._hover(False))
        for child in widget.winfo_children():
            self._bind_hover(child)

    def _hover(self, entering: bool) -> None:
        self.configure(fg_color=BG_ROW_HOV if entering else self._bg)

    def _agregar(self) -> None:
        try:
            agregar_figurita(self._data["num_figura"], self._data["cod_pais"])
            self._data["cantidad"] += 1
            self._actualizar_controles()
            self._on_change(self._data["num_figura"], self._data["cod_pais"])
        except Exception:
            pass

    def _quitar(self) -> None:
        try:
            quitar_figurita(self._data["num_figura"], self._data["cod_pais"])
            self._data["cantidad"] = max(0, self._data["cantidad"] - 1)
            if self._data["cantidad"] == 0:
                self._data["pegada"] = 0
            self._actualizar_controles()
            self._on_change(self._data["num_figura"], self._data["cod_pais"])
        except Exception:
            pass

    def _toggle_pegada(self) -> None:
        try:
            nueva = not bool(self._data["pegada"])
            marcar_pegada(self._data["num_figura"], self._data["cod_pais"], nueva)
            self._data["pegada"] = int(nueva)
            self._actualizar_controles()
            self._on_change(self._data["num_figura"], self._data["cod_pais"])
        except Exception:
            pass

    def _actualizar_controles(self) -> None:
        cantidad = self._data["cantidad"]
        pegada   = bool(self._data["pegada"])
        tiene    = cantidad > 0
        self.lbl_cantidad.configure(
            text=str(cantidad),
            text_color=VERDE_BTN if tiene else TEXTO_SEC,
        )
        self.btn_menos.configure(
            state="normal" if tiene else "disabled",
            fg_color=ROJO if tiene else ("#DDDDDD","#444444"),
        )
        self.btn_pegar.configure(
            state="normal" if tiene else "disabled",
            text="✅" if pegada else "□",
            fg_color=DORADO if pegada else "transparent",
            border_width=0 if pegada else 1,
            text_color=("#1C1C1E","#1C1C1E") if pegada else TEXTO_SEC,
        )