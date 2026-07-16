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
    marcar_pegadas_bulk,
    marcar_tengo_pais_bulk,
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

class _MouseWheelComboBox(ctk.CTkComboBox):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._scroll_dropdown: ctk.CTkToplevel | None = None
        self._scroll_dropdown_frame: ctk.CTkScrollableFrame | None = None

    def _open_dropdown_menu(self) -> None:
        if self._scroll_dropdown is not None and self._scroll_dropdown.winfo_exists():
            self._close_scroll_dropdown()
            return

        values = self.cget("values")
        if not values:
            return

        width = max(self.winfo_width(), self.cget("width"))
        row_height = 32
        max_visible_rows = 9
        height = min(len(values), max_visible_rows) * row_height + 8
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.winfo_height() + 3

        dropdown = ctk.CTkToplevel(self)
        dropdown.overrideredirect(True)
        dropdown.transient(self.winfo_toplevel())
        dropdown.geometry(f"{width}x{height}+{x}+{y}")
        dropdown.grid_rowconfigure(0, weight=1)
        dropdown.grid_columnconfigure(0, weight=1)

        try:
            dropdown.attributes("-topmost", True)
        except Exception:
            pass

        frame = ctk.CTkScrollableFrame(
            dropdown,
            width=width,
            height=height,
            corner_radius=8,
            fg_color=self.cget("dropdown_fg_color"),
            scrollbar_button_color=VERDE_MEDIO,
            scrollbar_button_hover_color=DORADO,
        )
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)

        dropdown_font = self.cget("dropdown_font")
        for value in values:
            btn = ctk.CTkButton(
                frame,
                text=value,
                height=30,
                corner_radius=6,
                anchor="w",
                fg_color="transparent",
                hover_color=self.cget("dropdown_hover_color"),
                text_color=self.cget("dropdown_text_color"),
                font=dropdown_font,
                command=lambda v=value: self._select_scroll_value(v),
            )
            btn.grid(row=len(frame.winfo_children()) - 1, column=0, padx=4, pady=1, sticky="ew")
            self._bind_dropdown_mousewheel(btn)

        self._scroll_dropdown = dropdown
        self._scroll_dropdown_frame = frame
        self._bind_dropdown_mousewheel(dropdown)
        self._bind_dropdown_mousewheel(frame)
        self._bind_dropdown_mousewheel(frame._parent_canvas)

        dropdown.bind("<Escape>", lambda _event: self._close_scroll_dropdown())
        dropdown.bind("<FocusOut>", self._schedule_dropdown_close)
        dropdown.focus_force()

    def _select_scroll_value(self, value: str) -> None:
        self._close_scroll_dropdown()
        self._dropdown_callback(value)

    def _schedule_dropdown_close(self, _event=None) -> None:
        if self._scroll_dropdown is not None and self._scroll_dropdown.winfo_exists():
            self.after(120, self._close_dropdown_if_focus_left)

    def _close_dropdown_if_focus_left(self) -> None:
        dropdown = self._scroll_dropdown
        if dropdown is None or not dropdown.winfo_exists():
            return

        focused = self.focus_get()
        if focused is None or not self._is_child_of(focused, dropdown):
            self._close_scroll_dropdown()

    def _is_child_of(self, widget, parent) -> bool:
        while widget is not None:
            if widget == parent:
                return True
            widget = getattr(widget, "master", None)
        return False

    def _bind_dropdown_mousewheel(self, widget) -> None:
        widget.bind("<MouseWheel>", self._on_dropdown_mousewheel, add="+")
        widget.bind("<Button-4>", self._on_dropdown_mousewheel, add="+")
        widget.bind("<Button-5>", self._on_dropdown_mousewheel, add="+")

    def _on_dropdown_mousewheel(self, event):
        frame = self._scroll_dropdown_frame
        if frame is None:
            return "break"

        if getattr(event, "num", None) == 4:
            units = -3
        elif getattr(event, "num", None) == 5:
            units = 3
        else:
            units = -int(event.delta / 120) if event.delta else 0

        if units:
            frame._parent_canvas.yview_scroll(units, "units")
        return "break"

    def _close_scroll_dropdown(self) -> None:
        if self._scroll_dropdown is not None and self._scroll_dropdown.winfo_exists():
            self._scroll_dropdown.destroy()
        self._scroll_dropdown = None
        self._scroll_dropdown_frame = None

    def destroy(self) -> None:
        self._close_scroll_dropdown()
        super().destroy()

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
        self._build_country_nav()

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
            text="Pais/seccion:",
            font=ctk.CTkFont(size=13),
            text_color=TEXTO_SEC,
        ).grid(row=0, column=0, padx=(16, 6), pady=10, sticky="w")

        nombres = [f"{p.cod_pais} — {p.nombre}" for p in self._paises]
        self.combo_pais = _MouseWheelComboBox(
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

        self.btn_pegar_disponibles = ctk.CTkButton(
            bar,
            text="Pegar disponibles",
            width=160,
            height=34,
            corner_radius=8,
            fg_color=DORADO,
            hover_color=DORADO_HOVER,
            text_color=("#1C1C1E", "#1C1C1E"),
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self._pegar_disponibles,
            state="disabled",
        )
        self.btn_tengo_todas = ctk.CTkButton(
            bar,
            text="Tengo todas",
            width=140,
            height=34,
            corner_radius=8,
            fg_color=VERDE_BTN,
            hover_color=VERDE_BTN_HOV,
            text_color=("#FFFFFF", "#FFFFFF"),
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self._toggle_tengo_todas,
            state="disabled",
        )
        self.btn_tengo_todas.grid(row=0, column=2, padx=(0, 8), pady=10, sticky="e")

        self.btn_pegar_disponibles.grid(row=0, column=3, padx=(0, 16), pady=10, sticky="e")

        prog_frame = ctk.CTkFrame(bar, fg_color="transparent")
        prog_frame.grid(row=0, column=4, padx=(0, 16), pady=10, sticky="e")

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
        self.scroll.grid(row=2, column=0, padx=16, pady=(12, 8), sticky="nsew")

        for c in range(STICKER_COLS):
            self.scroll.grid_columnconfigure(c, weight=1, uniform="sc")

    def _build_country_nav(self) -> None:
        footer = ctk.CTkFrame(
            self,
            fg_color=BG_MAIN,
            corner_radius=0,
            height=58,
        )
        footer.grid(row=3, column=0, sticky="ew")
        footer.grid_propagate(False)

        nav_frame = ctk.CTkFrame(footer, fg_color="transparent")
        nav_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.btn_pais_anterior = ctk.CTkButton(
            nav_frame,
            text="< Pais anterior",
            width=150,
            height=36,
            corner_radius=8,
            fg_color=VERDE_BTN,
            hover_color=VERDE_BTN_HOV,
            text_color=("#FFFFFF", "#FFFFFF"),
            font=ctk.CTkFont(size=13, weight="bold"),
            command=lambda: self._navegar_pais(-1),
            state="disabled",
        )
        self.btn_pais_anterior.grid(row=0, column=0, padx=(0, 8))

        self.btn_pais_siguiente = ctk.CTkButton(
            nav_frame,
            text="Pais siguiente >",
            width=150,
            height=36,
            corner_radius=8,
            fg_color=VERDE_BTN,
            hover_color=VERDE_BTN_HOV,
            text_color=("#FFFFFF", "#FFFFFF"),
            font=ctk.CTkFont(size=13, weight="bold"),
            command=lambda: self._navegar_pais(1),
            state="disabled",
        )
        self.btn_pais_siguiente.grid(row=0, column=1, padx=(8, 0))

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
        self._actualizar_botones_nav()

    def _indice_pais_actual(self) -> int:
        for idx, pais in enumerate(self._paises):
            if pais.cod_pais == self._cod_pais:
                return idx
        return -1

    def _navegar_pais(self, direccion: int) -> None:
        idx = self._indice_pais_actual()
        nuevo_idx = idx + direccion

        if idx < 0 or nuevo_idx < 0 or nuevo_idx >= len(self._paises):
            return

        self.set_country(self._paises[nuevo_idx].cod_pais)
        try:
            self.scroll._parent_canvas.yview_moveto(0)
        except Exception:
            pass

    def _actualizar_botones_nav(self) -> None:
        idx = self._indice_pais_actual()
        hay_anterior = idx > 0
        hay_siguiente = 0 <= idx < len(self._paises) - 1

        self.btn_pais_anterior.configure(
            state="normal" if hay_anterior else "disabled"
        )
        self.btn_pais_siguiente.configure(
            state="normal" if hay_siguiente else "disabled"
        )

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
            disponibles_para_pegar = max(0, resumen.tengo - resumen.pegadas)
            tengo_todas_sin_pegar = (
                resumen.total > 0
                and resumen.tengo == resumen.total
                and resumen.pegadas == 0
            )
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
            self.btn_pegar_disponibles.configure(
                state="normal" if disponibles_para_pegar > 0 else "disabled",
                text=(
                    f"Pegar disponibles ({disponibles_para_pegar})"
                    if disponibles_para_pegar > 0
                    else "Pegar disponibles"
                ),
            )
            self.btn_tengo_todas.configure(
                state="normal" if resumen.total > 0 else "disabled",
                text="Quitar todas" if tengo_todas_sin_pegar else "Tengo todas",
            )
        else:
            self.lbl_resumen.configure(text="Sin datos")
            self.prog_pais.set(0)
            self.lbl_pct_pais.configure(text="0%")
            self.btn_pegar_disponibles.configure(
                state="disabled",
                text="Pegar disponibles",
            )
            self.btn_tengo_todas.configure(
                state="disabled",
                text="Tengo todas",
            )

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

    def _pegar_disponibles(self) -> None:
        if not self._cod_pais:
            return

        items = [
            (card.num_figura, card.cod_pais)
            for card in self._cards
            if card.tiene and not card.pegada
        ]
        if not items:
            return

        marcadas = marcar_pegadas_bulk(items)
        if marcadas == 0:
            return

        for card in self._cards:
            if card.tiene:
                card.marcar_pegada_local()

        self._on_card_changed()

    def _toggle_tengo_todas(self) -> None:
        if not self._cod_pais:
            return

        try:
            resumen = obtener_resumen_pais(self._cod_pais)
        except Exception:
            return

        if not resumen:
            return

        tengo_todas_sin_pegar = (
            resumen.total > 0
            and resumen.tengo == resumen.total
            and resumen.pegadas == 0
        )
        marcar_tengo_pais_bulk(self._cod_pais, not tengo_todas_sin_pegar)
        self._cargar_pais(self._cod_pais)
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

    @property
    def num_figura(self) -> int:
        return self._fig.num_figura

    @property
    def cod_pais(self) -> str:
        return self._fig.cod_pais

    @property
    def tiene(self) -> bool:
        return self._item.cantidad > 0

    @property
    def pegada(self) -> bool:
        return self._item.pegada

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
            fg_color=DORADO if self._item.pegada else "transparent",
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

    def marcar_pegada_local(self) -> None:
        if not self.tiene:
            return
        self._item.pegada = True
        self._actualizar_ui()

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
            fg_color=DORADO if item.pegada else "transparent",
            border_width=0 if item.pegada else 1,
            text_color=(
                ("#1C1C1E", "#1C1C1E") if item.pegada else TEXTO_SEC
            ),
        )
