from __future__ import annotations
import customtkinter as ctk
from typing import TYPE_CHECKING

from models.collection_manager import (
    obtener_todos_los_paises,
    obtener_figuritas_de_pais,
    obtener_item_coleccion,
    obtener_resumen_pais,
    agregar_figurita,
    quitar_figurita,
    marcar_pegada,
)
from models.models import (
    Figurita,
    FiguritaJugador,
    FiguritaEspecial,
    ItemColeccion,
    Pais,
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
BG_CARD_HOV   = ("#F0F7F3", "#383838")
BG_CARD_TENE  = ("#EBF7F0", "#1E3A2A")   
BG_CARD_PEG   = ("#FFF8DC", "#3A3000")   
TEXTO_PRI     = ("#1C1C1E", "#F5F5F5")
TEXTO_SEC     = ("#555555", "#AAAAAA")
BORDE         = ("#D0D0D0", "#3A3A3C")
BORDE_TENE    = ("#80C9A0", "#2E6045")
BORDE_PEG     = ("#D4A830", "#8A6A00")
ROJO          = ("#CC2222", "#FF5555")
ROJO_HOVER    = ("#AA1111", "#DD3333")
VERDE_BTN     = ("#2E7D52", "#3A9E6A")
VERDE_BTN_HOV = ("#1A5C3A", "#2E8055")

STICKER_COLS = 4

class CountryView(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, main_window: "MainWindow") -> None:
        super().__init__(parent, fg_color=BG_MAIN, corner_radius=0)
        self.main_window = main_window

        self._cod_pais: str = ""
        self._paises: list[Pais] = []
        self._cards: list[_StickerCard] = []

        try:
            self._paises = obtener_todos_los_paises()
        except Exception:
            self._paises = []

        self._build()

    def _build(self) -> None:
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._build_header()
        self._build_control_bar()
        self._build_sticker_grid()

    def _build_header(self) -> None:
        header = ctk.CTkFrame(
            self,
            fg_color=VERDE_OSCURO,
            corner_radius=0,
            height=60,
        )
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)
        header.grid_columnconfigure(1, weight=1)

        btn_volver = ctk.CTkButton(
            header,
            text="← Volver",
            width=90,
            height=32,
            corner_radius=8,
            fg_color="transparent",
            hover_color=VERDE_MEDIO,
            text_color=("#FFFFFF", "#FFFFFF"),
            font=ctk.CTkFont(size=13),
            command=lambda: self.main_window.navigate_to("dashboard"),
        )
        btn_volver.grid(row=0, column=0, padx=(16, 8), pady=14, sticky="w")

        self.lbl_pais = ctk.CTkLabel(
            header,
            text="Selecciona un país",
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color=DORADO,
            anchor="w",
        )
        self.lbl_pais.grid(row=0, column=1, padx=8, pady=14, sticky="w")

        self.lbl_resumen = ctk.CTkLabel(
            header,
            text="",
            font=ctk.CTkFont(size=12),
            text_color=("#CCCCCC", "#AAAAAA"),
            anchor="e",
        )
        self.lbl_resumen.grid(row=0, column=2, padx=(0, 16), pady=14, sticky="e")

    def _build_control_bar(self) -> None:
        bar = ctk.CTkFrame(
            self,
            fg_color=BG_CARD,
            corner_radius=0,
            height=52,
            border_width=0,
        )
        bar.grid(row=1, column=0, sticky="ew")
        bar.grid_propagate(False)
        bar.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            bar,
            text="Equipo:",
            font=ctk.CTkFont(size=13),
            text_color=TEXTO_SEC,
        ).grid(row=0, column=0, padx=(16, 6), pady=10, sticky="w")

        nombres = [f"{p.cod_pais} — {p.nombre}" for p in self._paises]
        self.combo_pais = ctk.CTkComboBox(
            bar,
            values=nombres if nombres else ["Sin datos"],
            width=240,
            height=34,
            corner_radius=8,
            border_color=BORDE,
            button_color=VERDE_MEDIO,
            button_hover_color=VERDE_OSCURO,
            dropdown_hover_color=VERDE_CLARO,
            font=ctk.CTkFont(size=13),
            command=self._on_combo_changed,
            state="readonly",
        )
        self.combo_pais.grid(row=0, column=1, padx=(0, 16), pady=10, sticky="w")

        prog_frame = ctk.CTkFrame(bar, fg_color="transparent")
        prog_frame.grid(row=0, column=2, padx=(0, 16), pady=10, sticky="e")

        self.lbl_pct_pais = ctk.CTkLabel(
            prog_frame,
            text="",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=VERDE_OSCURO,
            width=42,
            anchor="e",
        )
        self.lbl_pct_pais.pack(side="left", padx=(0, 6))

        self.prog_pais = ctk.CTkProgressBar(
            prog_frame,
            width=160,
            height=10,
            corner_radius=5,
            fg_color=("#E0E0E0", "#3A3A3C"),
            progress_color=DORADO,
        )
        self.prog_pais.set(0)
        self.prog_pais.pack(side="left")

    def _build_sticker_grid(self) -> None:
        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color=BG_MAIN,
            corner_radius=0,
            scrollbar_button_color=VERDE_MEDIO,
            scrollbar_button_hover_color=DORADO,
        )
        self.scroll.grid(row=2, column=0, padx=16, pady=12, sticky="nsew")

        for c in range(STICKER_COLS):
            self.scroll.grid_columnconfigure(c, weight=1, uniform="sc")

    def set_country(self, cod_pais: str) -> None:
        if cod_pais == self._cod_pais:
            return  

        self._cod_pais = cod_pais
        self._sincronizar_combo(cod_pais)
        self._cargar_pais(cod_pais)

    def refresh(self) -> None:
        if self._cod_pais:
            self._cargar_pais(self._cod_pais)

    def _on_combo_changed(self, seleccion: str) -> None:
        cod = seleccion.split("—")[0].strip()
        if cod and cod != self._cod_pais:
            self._cod_pais = cod
            self._cargar_pais(cod)

    def _sincronizar_combo(self, cod_pais: str) -> None:
        for p in self._paises:
            if p.cod_pais == cod_pais:
                self.combo_pais.set(f"{p.cod_pais} — {p.nombre}")
                return

    def _cargar_pais(self, cod_pais: str) -> None:
        try:
            figuritas = obtener_figuritas_de_pais(cod_pais)
            resumen   = obtener_resumen_pais(cod_pais)
        except Exception as e:
            self._mostrar_error(str(e))
            return

        self._actualizar_header(cod_pais, resumen)
        self._poblar_grid(figuritas, cod_pais)

    def _actualizar_header(self, cod_pais: str, resumen) -> None:
        from views.dashboard_view import _flag_emoji   
        bandera = _flag_emoji(cod_pais)

        nombre = cod_pais
        for p in self._paises:
            if p.cod_pais == cod_pais:
                nombre = p.nombre
                break

        self.lbl_pais.configure(text=f"{bandera}  {nombre}")

        if resumen:
            self.lbl_resumen.configure(
                text=(
                    f"{resumen.pegadas}/{resumen.total} pegadas  ·  "
                    f"{resumen.faltan} faltan  ·  "
                    f"{resumen.repetidas} repetidas"
                )
            )
            pct = resumen.porcentaje / 100
            self.prog_pais.set(pct)
            self.lbl_pct_pais.configure(text=f"{resumen.porcentaje:.0f}%")
        else:
            self.lbl_resumen.configure(text="Sin datos")
            self.prog_pais.set(0)
            self.lbl_pct_pais.configure(text="0%")

    def _poblar_grid(self, figuritas: list[Figurita], cod_pais: str) -> None:
        for card in self._cards:
            card.destroy()
        self._cards.clear()

        for idx, fig in enumerate(figuritas):
            item = obtener_item_coleccion(fig.num_figura, fig.cod_pais)
            fila = idx // STICKER_COLS
            col  = idx % STICKER_COLS

            card = _StickerCard(
                self.scroll,
                figurita=fig,
                item=item,
                on_change=self._on_card_changed,
            )
            card.grid(row=fila, column=col, padx=6, pady=6, sticky="nsew")
            self._cards.append(card)

    def _on_card_changed(self) -> None:
        try:
            resumen = obtener_resumen_pais(self._cod_pais)
            self._actualizar_header(self._cod_pais, resumen)
        except Exception:
            pass

        self.main_window.on_collection_changed()

    def _mostrar_error(self, msg: str) -> None:
        ctk.CTkLabel(
            self,
            text=f"Error al cargar el equipo:\n{msg}",
            font=ctk.CTkFont(size=13),
            text_color=("#CC0000", "#FF6666"),
        ).grid(row=2, column=0, pady=40)

class _StickerCard(ctk.CTkFrame):
    def __init__(
        self,
        parent: ctk.CTkFrame,
        figurita: Figurita,
        item: ItemColeccion,
        on_change: callable,
    ) -> None:
        fg, border = self._colores_por_estado(item)
        super().__init__(
            parent,
            fg_color=fg,
            corner_radius=10,
            border_width=1,
            border_color=border,
        )
        self._fig      = figurita
        self._item     = item
        self._on_change = on_change

        self._build()

    def _build(self) -> None:
        self.grid_columnconfigure(0, weight=1)

        self._build_info_row()
        self._build_controls_row()

    def _build_info_row(self) -> None:
        row = ctk.CTkFrame(self, fg_color="transparent")
        row.grid(row=0, column=0, padx=10, pady=(10, 4), sticky="ew")
        row.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            row,
            text=f"#{self._fig.num_figura}",
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color=VERDE_OSCURO,
            text_color=("#FFFFFF", "#FFFFFF"),
            corner_radius=5,
            padx=5,
            pady=2,
            width=42,
        ).grid(row=0, column=0, sticky="w")

        nombre = self._nombre_figurita()
        if len(nombre) > 18:
            nombre = nombre[:16] + "…"

        ctk.CTkLabel(
            row,
            text=nombre,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=TEXTO_PRI,
            anchor="w",
        ).grid(row=0, column=1, padx=(6, 0), sticky="w")

    def _build_controls_row(self) -> None:
        row = ctk.CTkFrame(self, fg_color="transparent")
        row.grid(row=1, column=0, padx=8, pady=(0, 10), sticky="ew")
        row.grid_columnconfigure(0, weight=1)

        self.lbl_estado = ctk.CTkLabel(
            row,
            text=self._item.estado,
            font=ctk.CTkFont(size=10),
            text_color=TEXTO_SEC,
            anchor="w",
        )
        self.lbl_estado.grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 4))

        self.btn_menos = ctk.CTkButton(
            row,
            text="−",
            width=28,
            height=28,
            corner_radius=6,
            fg_color=ROJO if self._item.cantidad > 0 else ("#E0E0E0", "#444444"),
            hover_color=ROJO_HOVER,
            text_color=("#FFFFFF", "#FFFFFF"),
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self._quitar,
            state="normal" if self._item.cantidad > 0 else "disabled",
        )
        self.btn_menos.grid(row=1, column=0, sticky="w")

        self.lbl_cantidad = ctk.CTkLabel(
            row,
            text=str(self._item.cantidad),
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=TEXTO_PRI,
            width=28,
            anchor="center",
        )
        self.lbl_cantidad.grid(row=1, column=1, padx=4)

        self.btn_mas = ctk.CTkButton(
            row,
            text="+",
            width=28,
            height=28,
            corner_radius=6,
            fg_color=VERDE_BTN,
            hover_color=VERDE_BTN_HOV,
            text_color=("#FFFFFF", "#FFFFFF"),
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self._agregar,
        )
        self.btn_mas.grid(row=1, column=2, padx=(0, 6))

        self.btn_pegar = ctk.CTkButton(
            row,
            text="✅" if self._item.pegada else "□",
            width=28,
            height=28,
            corner_radius=6,
            fg_color=DORADO if self._item.pegada else ("transparent", "transparent"),
            hover_color=DORADO_HOVER,
            border_width=1 if not self._item.pegada else 0,
            border_color=BORDE,
            text_color=("#1C1C1E", "#1C1C1E") if self._item.pegada else TEXTO_SEC,
            font=ctk.CTkFont(size=14),
            command=self._toggle_pegada,
            state="normal" if self._item.cantidad > 0 else "disabled",
        )
        self.btn_pegar.grid(row=1, column=3, sticky="e")

    def _nombre_figurita(self) -> str:
        if isinstance(self._fig, FiguritaJugador):
            return self._fig.nombre_completo
        if isinstance(self._fig, FiguritaEspecial):
            return self._fig.tipo_especial or "Especial"
        return f"Figurita {self._fig.num_figura}"

    @staticmethod
    def _colores_por_estado(item: ItemColeccion) -> tuple[tuple, tuple]:
        if item.pegada:
            return BG_CARD_PEG, BORDE_PEG
        if item.tiene:
            return BG_CARD_TENE, BORDE_TENE
        return BG_CARD, BORDE

    def _agregar(self) -> None:
        try:
            agregar_figurita(self._fig.num_figura, self._fig.cod_pais)
            self._item = obtener_item_coleccion(
                self._fig.num_figura, self._fig.cod_pais
            )
            self._actualizar_ui()
            self._on_change()
        except Exception:
            pass

    def _quitar(self) -> None:
        try:
            quitar_figurita(self._fig.num_figura, self._fig.cod_pais)
            self._item = obtener_item_coleccion(
                self._fig.num_figura, self._fig.cod_pais
            )
            self._actualizar_ui()
            self._on_change()
        except Exception:
            pass

    def _toggle_pegada(self) -> None:
        try:
            nueva = not self._item.pegada
            marcar_pegada(self._fig.num_figura, self._fig.cod_pais, nueva)
            self._item = obtener_item_coleccion(
                self._fig.num_figura, self._fig.cod_pais
            )
            self._actualizar_ui()
            self._on_change()
        except Exception:
            pass

    def _actualizar_ui(self) -> None:
        item = self._item

        fg, border = self._colores_por_estado(item)
        self.configure(fg_color=fg, border_color=border)

        self.lbl_estado.configure(text=item.estado)

        self.lbl_cantidad.configure(text=str(item.cantidad))

        tiene = item.cantidad > 0
        self.btn_menos.configure(
            state="normal" if tiene else "disabled",
            fg_color=ROJO if tiene else ("#E0E0E0", "#444444"),
        )

        self.btn_pegar.configure(
            state="normal" if tiene else "disabled",
            text="✅" if item.pegada else "□",
            fg_color=DORADO if item.pegada else ("transparent", "transparent"),
            border_width=0 if item.pegada else 1,
            text_color=(
                ("#1C1C1E", "#1C1C1E") if item.pegada else TEXTO_SEC
            ),
        )