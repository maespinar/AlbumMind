from __future__ import annotations
import customtkinter as ctk
from typing import TYPE_CHECKING

from models.collection_manager import (
    obtener_resumen_global,
    obtener_resumen_por_pais,
)
from models.models import ResumenPais, ResumenColeccion

if TYPE_CHECKING:
    from views.main_window import MainWindow

VERDE_OSCURO = ("#1A4731", "#0F2E20")
VERDE_MEDIO  = ("#236040", "#1A4731")
VERDE_CLARO  = ("#E8F5EE", "#1E3A2A")
DORADO       = ("#F5C842", "#F5C842")
DORADO_HOVER = ("#D4A830", "#D4A830")
BG_MAIN      = ("#F4F6F3", "#1C1C1E")
BG_CARD      = ("#FFFFFF", "#2C2C2E")
BG_CARD_HOV  = ("#F0F7F3", "#383838")
TEXTO_PRI    = ("#1C1C1E", "#F5F5F5")
TEXTO_SEC    = ("#555555", "#AAAAAA")
BORDE        = ("#D0D0D0", "#3A3A3C")
VERDE_PROG   = ("#2E7D52", "#3A9E6A")   
ROJO_VACIO   = ("#E0E0E0", "#3A3A3C")   

CARD_W = 160
GRID_COLS = 6

_ISO3_TO_ISO2 = {
    "ALG": "DZ", "ARG": "AR", "AUS": "AU", "AUT": "AT",
    "BEL": "BE", "BIH": "BA", "BRA": "BR", "CAN": "CA",
    "CIV": "CI", "COD": "CD", "COL": "CO", "CPV": "CV",
    "CRO": "HR", "CUW": "CW", "CZE": "CZ", "ECU": "EC",
    "EGY": "EG", "ENG": "GB", "ESP": "ES", "FRA": "FR",
    "GER": "DE", "GHA": "GH", "HAI": "HT", "IRN": "IR",
    "IRQ": "IQ", "JOR": "JO", "JPN": "JP", "KOR": "KR",
    "KSA": "SA", "MAR": "MA", "MEX": "MX", "NED": "NL",
    "NOR": "NO", "NZL": "NZ", "PAN": "PA", "PAR": "PY",
    "POR": "PT", "QAT": "QA", "RSA": "ZA", "SCO": "GB",
    "SEN": "SN", "SUI": "CH", "SWE": "SE", "TUN": "TN",
    "TUR": "TR", "URU": "UY", "USA": "US", "UZB": "UZ",
}

def _flag_emoji(cod_pais: str) -> str:
    iso2 = _ISO3_TO_ISO2.get(cod_pais.upper(), "")
    if not iso2:
        return "🏳️"
    return "".join(chr(0x1F1E6 + ord(c) - ord("A")) for c in iso2.upper())

def _color_por_porcentaje(pct: float) -> str:
    if pct >= 100:
        return "#F5C842"   # dorado: completo
    if pct >= 75:
        return "#2E7D52"   # verde oscuro: casi completo
    if pct >= 40:
        return "#4CAF7D"   # verde medio
    if pct > 0:
        return "#81C784"   # verde claro: iniciado
    return "#9E9E9E"       # gris: sin figuritas

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, main_window: "MainWindow") -> None:
        super().__init__(parent, fg_color=BG_MAIN, corner_radius=0)
        self.main_window = main_window
        self._filtro_activo: str = "todos" 
        self._resumen_paises: list[ResumenPais] = []
        self._tarjetas: list[_CountryCard] = []
        self._build()
        self.refresh()

    def _build(self) -> None:
        self.grid_rowconfigure(3, weight=1)   
        self.grid_columnconfigure(0, weight=1)

        self._build_header()
        self._build_stats_row()
        self._build_filter_bar()
        self._build_country_grid()

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, padx=24, pady=(20, 8), sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header,
            text="Mi colección",
            font=ctk.CTkFont(family="Arial", size=26, weight="bold"),
            text_color=TEXTO_PRI,
            anchor="w",
        ).grid(row=0, column=0, sticky="w")

        self.lbl_subtitulo = ctk.CTkLabel(
            header,
            text="FIFA World Cup 2026 — Álbum Panini oficial",
            font=ctk.CTkFont(size=13),
            text_color=TEXTO_SEC,
            anchor="w",
        )
        self.lbl_subtitulo.grid(row=1, column=0, sticky="w")

    def _build_stats_row(self) -> None:
        stats_outer = ctk.CTkFrame(self, fg_color="transparent")
        stats_outer.grid(row=1, column=0, padx=24, pady=(4, 12), sticky="ew")
        stats_outer.grid_columnconfigure((0, 1, 2, 3), weight=1)
        stat_defs = [
            ("lbl_pegadas",   "✅  Pegadas",   "0",  VERDE_OSCURO),
            ("lbl_tengo",     "📦  En mano",   "0",  VERDE_MEDIO),
            ("lbl_faltan",    "❌  Faltan",    "980", ("#7B3F00", "#A0522D")),
            ("lbl_repetidas", "🔁  Repetidas", "0",  ("#1A3A5C", "#1E4A7A")),
        ]
        self._stat_labels: dict[str, ctk.CTkLabel] = {}

        for col, (attr, titulo, valor_defecto, color) in enumerate(stat_defs):
            card = ctk.CTkFrame(
                stats_outer,
                fg_color=BG_CARD,
                corner_radius=12,
                border_width=1,
                border_color=BORDE,
            )
            card.grid(row=0, column=col, padx=(0, 10) if col < 3 else 0, sticky="ew")
            card.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(
                card,
                text=titulo,
                font=ctk.CTkFont(size=11),
                text_color=TEXTO_SEC,
                anchor="w",
            ).grid(row=0, column=0, padx=14, pady=(12, 2), sticky="w")

            lbl_val = ctk.CTkLabel(
                card,
                text=valor_defecto,
                font=ctk.CTkFont(family="Arial", size=28, weight="bold"),
                text_color=color,
                anchor="w",
            )
            lbl_val.grid(row=1, column=0, padx=14, pady=(0, 12), sticky="w")
            self._stat_labels[attr] = lbl_val

        prog_frame = ctk.CTkFrame(
            stats_outer,
            fg_color=BG_CARD,
            corner_radius=12,
            border_width=1,
            border_color=BORDE,
        )
        prog_frame.grid(row=1, column=0, columnspan=4, pady=(8, 0), sticky="ew")
        prog_frame.grid_columnconfigure(1, weight=1)

        self.lbl_pct = ctk.CTkLabel(
            prog_frame,
            text="0%",
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color=VERDE_OSCURO,
            width=56,
        )
        self.lbl_pct.grid(row=0, column=0, padx=(16, 8), pady=12)

        self.prog_grande = ctk.CTkProgressBar(
            prog_frame,
            height=18,
            corner_radius=9,
            fg_color=("#E0E0E0", "#3A3A3C"),
            progress_color=DORADO,
        )
        self.prog_grande.set(0)
        self.prog_grande.grid(row=0, column=1, padx=(0, 16), pady=12, sticky="ew")

    def _build_filter_bar(self) -> None:
        bar = ctk.CTkFrame(self, fg_color="transparent")
        bar.grid(row=2, column=0, padx=24, pady=(0, 10), sticky="ew")

        filtros = [
            ("todos",         "Todos los países"),
            ("con_figuritas", "Con figuritas"),
            ("completos",     "Completos ✨"),
        ]
        self._filter_btns: dict[str, ctk.CTkButton] = {}

        for key, label in filtros:
            btn = ctk.CTkButton(
                bar,
                text=label,
                width=140,
                height=30,
                corner_radius=15,
                border_width=1,
                border_color=BORDE,
                fg_color="transparent",
                hover_color=VERDE_CLARO,
                text_color=TEXTO_PRI,
                font=ctk.CTkFont(size=12),
                command=lambda k=key: self._aplicar_filtro(k),
            )
            btn.pack(side="left", padx=(0, 8))
            self._filter_btns[key] = btn

        self._marcar_filtro_activo("todos")

    def _build_country_grid(self) -> None:
        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color=BG_MAIN,
            corner_radius=0,
            scrollbar_button_color=VERDE_MEDIO,
            scrollbar_button_hover_color=DORADO,
        )
        self.scroll.grid(row=3, column=0, padx=12, pady=(0, 12), sticky="nsew")

        for c in range(GRID_COLS):
            self.scroll.grid_columnconfigure(c, weight=1, uniform="col")

    def refresh(self) -> None:
        try:
            resumen_global = obtener_resumen_global()
            self._resumen_paises = obtener_resumen_por_pais()
        except Exception as e:
            self._mostrar_error(str(e))
            return

        self._actualizar_stats(resumen_global)
        self._aplicar_filtro(self._filtro_activo)

    def _actualizar_stats(self, r: ResumenColeccion) -> None:
        self._stat_labels["lbl_pegadas"].configure(text=str(r.total_pegadas))
        self._stat_labels["lbl_tengo"].configure(text=str(r.total_tengo))
        self._stat_labels["lbl_faltan"].configure(text=str(r.total_faltan))
        self._stat_labels["lbl_repetidas"].configure(text=str(r.total_repetidas))

        pct = r.porcentaje
        self.prog_grande.set(pct / 100)
        self.lbl_pct.configure(text=f"{pct:.1f}%")
        self.lbl_subtitulo.configure(
            text=(
                f"FIFA World Cup 2026 — Álbum Panini oficial  ·  "
                f"{r.total_figuritas} figuritas totales"
            )
        )

    def _aplicar_filtro(self, filtro: str) -> None:
        self._filtro_activo = filtro
        self._marcar_filtro_activo(filtro)

        if filtro == "con_figuritas":
            paises = [r for r in self._resumen_paises if r.tengo > 0]
        elif filtro == "completos":
            paises = [r for r in self._resumen_paises if r.completo]
        else:
            paises = self._resumen_paises

        self._poblar_grid(paises)

    def _marcar_filtro_activo(self, activo: str) -> None:
        for key, btn in self._filter_btns.items():
            if key == activo:
                btn.configure(
                    fg_color=VERDE_OSCURO,
                    text_color=("#FFFFFF", "#FFFFFF"),
                    border_color=VERDE_OSCURO,
                    font=ctk.CTkFont(size=12, weight="bold"),
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=TEXTO_PRI,
                    border_color=BORDE,
                    font=ctk.CTkFont(size=12, weight="normal"),
                )

    def _poblar_grid(self, paises: list[ResumenPais]) -> None:
        for tarjeta in self._tarjetas:
            tarjeta.destroy()
        self._tarjetas.clear()

        if not paises:
            self._mostrar_vacio()
            return

        for idx, rp in enumerate(paises):
            fila = idx // GRID_COLS
            col  = idx % GRID_COLS

            tarjeta = _CountryCard(
                self.scroll,
                resumen=rp,
                on_click=lambda cod=rp.cod_pais: self.main_window.navigate_to_country(cod),
            )
            tarjeta.grid(row=fila, column=col, padx=6, pady=6, sticky="nsew")
            self._tarjetas.append(tarjeta)

    def _mostrar_vacio(self) -> None:
        lbl = ctk.CTkLabel(
            self.scroll,
            text="No hay países que coincidan con el filtro.",
            font=ctk.CTkFont(size=14),
            text_color=TEXTO_SEC,
        )
        lbl.grid(row=0, column=0, columnspan=GRID_COLS, pady=40)
        self._tarjetas.append(lbl)  

    def _mostrar_error(self, msg: str) -> None:
        ctk.CTkLabel(
            self,
            text=f"Error al cargar datos:\n{msg}",
            font=ctk.CTkFont(size=13),
            text_color=("#CC0000", "#FF6666"),
        ).grid(row=3, column=0, pady=40)

class _CountryCard(ctk.CTkFrame):
    HEIGHT = 130

    def __init__(
        self,
        parent: ctk.CTkFrame,
        resumen: ResumenPais,
        on_click: callable,
    ) -> None:
        super().__init__(
            parent,
            fg_color=BG_CARD,
            corner_radius=12,
            border_width=1,
            border_color=BORDE,
            cursor="hand2",
        )
        self._resumen = resumen
        self._on_click = on_click
        self._build()
        self._bind_click(self)

    def _build(self) -> None:
        r = self._resumen
        self.grid_columnconfigure(0, weight=1)

        top_row = ctk.CTkFrame(self, fg_color="transparent")
        top_row.grid(row=0, column=0, padx=12, pady=(10, 2), sticky="ew")
        top_row.grid_columnconfigure(0, weight=1)

        bandera = _flag_emoji(r.cod_pais)
        ctk.CTkLabel(
            top_row,
            text=f"{bandera}  {r.cod_pais}",
            font=ctk.CTkFont(size=18),
            text_color=TEXTO_PRI,
            anchor="w",
        ).grid(row=0, column=0, sticky="w")

        if r.completo:
            badge_color = ("#F5C842", "#F5C842")
            badge_text  = "✨ Completo"
            badge_tc    = ("#5A4000", "#5A4000")
        elif r.tengo > 0:
            badge_color = VERDE_CLARO
            badge_text  = f"+{r.repetidas} rep." if r.repetidas > 0 else ""
            badge_tc    = VERDE_OSCURO
        else:
            badge_color = ("transparent", "transparent")
            badge_text  = ""
            badge_tc    = TEXTO_SEC

        if badge_text:
            ctk.CTkLabel(
                top_row,
                text=badge_text,
                font=ctk.CTkFont(size=10, weight="bold"),
                fg_color=badge_color,
                text_color=badge_tc,
                corner_radius=6,
                padx=6,
                pady=2,
            ).grid(row=0, column=1, sticky="e")

        nombre = r.nombre_pais
        if len(nombre) > 16:
            nombre = nombre[:14] + "…"

        ctk.CTkLabel(
            self,
            text=nombre,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=TEXTO_PRI,
            anchor="w",
        ).grid(row=1, column=0, padx=12, sticky="w")

        ctk.CTkLabel(
            self,
            text=f"{r.pegadas} / {r.total} figuritas",
            font=ctk.CTkFont(size=11),
            text_color=TEXTO_SEC,
            anchor="w",
        ).grid(row=2, column=0, padx=12, pady=(1, 4), sticky="w")

        barra = ctk.CTkProgressBar(
            self,
            height=7,
            corner_radius=4,
            fg_color=("#E0E0E0", "#3A3A3C"),
            progress_color=_color_por_porcentaje(r.porcentaje),
        )
        barra.set(r.porcentaje / 100 if r.total > 0 else 0)
        barra.grid(row=3, column=0, padx=12, pady=(0, 10), sticky="ew")

        self._bind_click(top_row)
        self._bind_click(barra)

    def _bind_click(self, widget) -> None:
        widget.bind("<Button-1>", lambda _e: self._on_click())
        widget.bind("<Enter>",    lambda _e: self._on_hover(True))
        widget.bind("<Leave>",    lambda _e: self._on_hover(False))
        for child in widget.winfo_children():
            self._bind_click(child)

    def _on_hover(self, entering: bool) -> None:
        self.configure(fg_color=BG_CARD_HOV if entering else BG_CARD)