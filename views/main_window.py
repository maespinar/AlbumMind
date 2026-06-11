import customtkinter as ctk
from models.collection_manager import obtener_resumen_global

VERDE_OSCURO  = ("#1A4731", "#0F2E20")   
VERDE_MEDIO   = ("#236040", "#1A4731")   
DORADO        = ("#F5C842", "#F5C842")   
DORADO_HOVER  = ("#D4A830", "#D4A830")
BLANCO_TEXTO  = ("#FFFFFF", "#FFFFFF")
BG_MAIN       = ("#F4F6F3", "#1C1C1E")   
BG_CARD       = ("#FFFFFF", "#2C2C2E")   
TEXTO_PRI     = ("#1C1C1E", "#F5F5F5")
TEXTO_SEC     = ("#555555", "#AAAAAA")
BORDE         = ("#D0D0D0", "#3A3A3C")

class MainWindow(ctk.CTk):
    SIDEBAR_W = 200
    def __init__(self) -> None:
        super().__init__()
        self.title("AlbumMind — FIFA World Cup 2026")
        self.geometry("1100x700")
        self.minsize(900, 600)
        ctk.set_appearance_mode("System")       
        ctk.set_default_color_theme("green")    
        # ── Estado de navegación 
        self._views: dict[str, ctk.CTkFrame] = {}
        self._current_view: str = ""
        self._nav_buttons: dict[str, ctk.CTkButton] = {}
        # ── Construir layout 
        self._build_layout()
        self._build_topbar()
        self._build_sidebar()
        self._build_content_area()
        # ── Vista inicial 
        self._show_view("dashboard")

    def _build_layout(self) -> None:
        self.grid_columnconfigure(0, weight=0, minsize=self.SIDEBAR_W)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.configure(fg_color=BG_MAIN)

    def _build_topbar(self) -> None:
        self.topbar = ctk.CTkFrame(
            self,
            height=56,
            corner_radius=0,
            fg_color=VERDE_OSCURO,
        )
        self.topbar.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.topbar.grid_propagate(False)
        self.topbar.grid_columnconfigure(1, weight=1)

        lbl_logo = ctk.CTkLabel(
            self.topbar,
            text="⚽  AlbumMind",
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color=DORADO,
        )
        lbl_logo.grid(row=0, column=0, padx=(20, 30), pady=0, sticky="w")

        progress_frame = ctk.CTkFrame(
            self.topbar,
            fg_color="transparent",
        )
        progress_frame.grid(row=0, column=1, padx=(0, 20), pady=0, sticky="e")
        progress_frame.grid_columnconfigure(0, weight=1)

        self.lbl_progreso = ctk.CTkLabel(
            progress_frame,
            text="Cargando...",
            font=ctk.CTkFont(size=12),
            text_color=BLANCO_TEXTO,
        )
        self.lbl_progreso.grid(row=0, column=0, sticky="e", padx=(0, 8))

        self.progress_bar = ctk.CTkProgressBar(
            progress_frame,
            width=220,
            height=10,
            corner_radius=5,
            fg_color=VERDE_MEDIO,
            progress_color=DORADO,
        )
        self.progress_bar.set(0)
        self.progress_bar.grid(row=0, column=1, sticky="e")

        self.refresh_topbar()

    def refresh_topbar(self) -> None:
        try:
            resumen = obtener_resumen_global()
            pct = resumen.porcentaje / 100
            self.progress_bar.set(pct)
            self.lbl_progreso.configure(
                text=(
                    f"{resumen.total_pegadas}/{resumen.total_figuritas} pegadas  "
                    f"({resumen.porcentaje}%)  ·  "
                    f"{resumen.total_faltan} faltan  ·  "
                    f"{resumen.total_repetidas} repetidas"
                )
            )
        except Exception:
            self.lbl_progreso.configure(text="Error al cargar estadísticas")

    def _build_sidebar(self) -> None:
        self.sidebar = ctk.CTkFrame(
            self,
            width=self.SIDEBAR_W,
            corner_radius=0,
            fg_color=VERDE_OSCURO,
        )
        self.sidebar.grid(row=1, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self.sidebar.grid_rowconfigure(10, weight=1)   

        nav_items = [
            ("dashboard",  "Dashboard",    "🏠"),
            ("countries",  "Por país",     "🌍"),
            ("search",     "Buscar",       "🔍"),
            ("export",     "Exportar",     "📄"),
        ]

        for idx, (key, label, icon) in enumerate(nav_items):
            btn = ctk.CTkButton(
                self.sidebar,
                text=f"  {icon}  {label}",
                anchor="w",
                height=44,
                corner_radius=8,
                border_width=0,
                fg_color="transparent",
                hover_color=VERDE_MEDIO,
                text_color=BLANCO_TEXTO,
                font=ctk.CTkFont(size=14),
                command=lambda k=key: self._show_view(k),
            )
            btn.grid(row=idx, column=0, padx=12, pady=(6, 2), sticky="ew")
            self._nav_buttons[key] = btn

        sep = ctk.CTkFrame(
            self.sidebar,
            height=1,
            fg_color=VERDE_MEDIO,
        )
        sep.grid(row=len(nav_items), column=0, padx=16, pady=12, sticky="ew")

        self._build_sidebar_footer()

    def _build_sidebar_footer(self) -> None:

        footer = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        footer.grid(row=11, column=0, padx=12, pady=(0, 16), sticky="ew")
        footer.grid_columnconfigure(0, weight=1)

        lbl_modo = ctk.CTkLabel(
            footer,
            text="Modo oscuro",
            font=ctk.CTkFont(size=12),
            text_color=TEXTO_SEC,
        )
        lbl_modo.grid(row=0, column=0, sticky="w")

        toggle = ctk.CTkSwitch(
            footer,
            text="",
            width=44,
            command=self._toggle_appearance,
            onvalue="Dark",
            offvalue="Light",
            button_color=DORADO,
            button_hover_color=DORADO_HOVER,
            progress_color=VERDE_MEDIO,
        )
        toggle.grid(row=0, column=1, sticky="e")
        if ctk.get_appearance_mode() == "Dark":
            toggle.select()

        ctk.CTkLabel(
            footer,
            text="v0.1.0",
            font=ctk.CTkFont(size=10),
            text_color=TEXTO_SEC,
        ).grid(row=1, column=0, columnspan=2, sticky="w", pady=(6, 0))

    def _toggle_appearance(self) -> None:
        current = ctk.get_appearance_mode()
        ctk.set_appearance_mode("Dark" if current == "Light" else "Light")

    def _build_content_area(self) -> None:
        self.content_area = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=BG_MAIN,
        )
        self.content_area.grid(row=1, column=1, sticky="nsew")
        self.content_area.grid_rowconfigure(0, weight=1)
        self.content_area.grid_columnconfigure(0, weight=1)

    def _show_view(self, name: str) -> None:
        if name == self._current_view:
            return

        if self._current_view and self._current_view in self._views:
            self._views[self._current_view].grid_remove()

        if name not in self._views:
            self._views[name] = self._create_view(name)

        self._views[name].grid(row=0, column=0, sticky="nsew")
        self._current_view = name

        self._update_nav_buttons(name)

    def _create_view(self, name: str) -> ctk.CTkFrame:
        parent = self.content_area

        if name == "dashboard":
            from views.dashboard_view import DashboardView
            return DashboardView(parent, main_window=self)

        if name == "countries":
            from views.country_view import CountryView
            return CountryView(parent, main_window=self)

        if name == "search":
            from views.search_view import SearchView
            return SearchView(parent, main_window=self)

        if name == "export":
            from views.export_view import ExportView
            return ExportView(parent, main_window=self)

        fallback = ctk.CTkFrame(parent, fg_color=BG_MAIN)
        ctk.CTkLabel(
            fallback,
            text=f"Vista '{name}' no encontrada.",
            text_color=TEXTO_SEC,
        ).pack(expand=True)
        return fallback

    def _update_nav_buttons(self, active: str) -> None:
        for key, btn in self._nav_buttons.items():
            if key == active:
                btn.configure(
                    fg_color=DORADO,
                    text_color=("#1C1C1E", "#1C1C1E"),
                    font=ctk.CTkFont(size=14, weight="bold"),
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=BLANCO_TEXTO,
                    font=ctk.CTkFont(size=14, weight="normal"),
                )

    def navigate_to(self, view_name: str) -> None:
        self._show_view(view_name)

    def navigate_to_country(self, cod_pais: str) -> None:
        if "countries" in self._views:
            self._views["countries"].set_country(cod_pais)
        self._show_view("countries")
        if "countries" in self._views:
            self._views["countries"].set_country(cod_pais)

    def on_collection_changed(self) -> None:
        self.refresh_topbar()

        current = self._views.get(self._current_view)
        if current and hasattr(current, "refresh"):
            current.refresh()