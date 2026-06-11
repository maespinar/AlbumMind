# ============================================================
#  AlbumMind — build.spec
#  Configuración de PyInstaller para generar el ejecutable.
#
#  CÓMO USAR:
#    1. Activa el entorno virtual:
#         Windows : venv\Scripts\activate
#         Mac/Linux: source venv/bin/activate
#
#    2. Desde la raíz del proyecto (donde está main.py):
#         pyinstaller build.spec
#
#    3. El ejecutable queda en:
#         dist/AlbumMind/AlbumMind.exe   (Windows)
#         dist/AlbumMind/AlbumMind       (Mac/Linux)
#
#  NOTAS IMPORTANTES:
#    • Este spec usa --onedir (carpeta), NO --onefile.
#      --onefile descomprime todo a %TEMP% en cada arranque,
#      lo que lo hace lento (~5s extra) y falla en algunos
#      antivirus corporativos. --onedir arranca en <1s.
#
#    • La BD albumind.db se crea junto al ejecutable en
#      dist/AlbumMind/ en el primer arranque. Ahí el usuario
#      puede hacer backups fácilmente.
#
#    • Para distribuir, comprime dist/AlbumMind/ completo en
#      un .zip. El usuario lo descomprime y ejecuta.
# ============================================================

import sys
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# ── Rutas base ────────────────────────────────────────────────
# SPEC_DIR es la carpeta donde vive este .spec (raíz del proyecto)
SPEC_DIR = os.path.dirname(os.path.abspath(SPEC))   # noqa: F821  (SPEC es variable de PyInstaller)


# ── 1. Archivos de datos a incluir (datas) ───────────────────
#
#  Formato de cada entrada: (origen, destino_dentro_del_bundle)
#  El destino es la ruta RELATIVA que verá resource_path() en main.py.

datas = [
    # Archivos SQL propios del proyecto
    (os.path.join(SPEC_DIR, "database", "schema.sql"),    "database"),
    (os.path.join(SPEC_DIR, "database", "seed_data.sql"), "database"),

    # Temas, fuentes e iconos de CustomTkinter (OBLIGATORIO)
    # Sin esto la app arranca con un error de "can't find theme file"
    *collect_data_files("customtkinter"),

    # Plantilla de documento de python-docx (OBLIGATORIO)
    # Sin esto exportar_*_docx() falla con FileNotFoundError
    *collect_data_files("docx"),
]


# ── 2. Imports ocultos (hiddenimports) ───────────────────────
#
#  PyInstaller analiza el código estáticamente y a veces no
#  detecta imports dinámicos o de plugins. Los listamos aquí.

hidden_imports = [
    # SQLite: el módulo _sqlite3 es una extensión C que PyInstaller
    # puede pasar por alto en algunos entornos
    "_sqlite3",

    # Tkinter y sus submódulos (CustomTkinter los usa internamente)
    "tkinter",
    "tkinter.ttk",
    "tkinter.filedialog",
    "tkinter.messagebox",
    "tkinter.font",

    # CustomTkinter: importa submódulos dinámicamente según el tema
    *collect_submodules("customtkinter"),

    # python-docx: carga lxml internamente
    "lxml",
    "lxml.etree",
    "lxml._elementpath",

    # Nuestros propios paquetes (por si el análisis estático los omite)
    "database",
    "database.database",
    "models",
    "models.models",
    "models.collection_manager",
    "models.exporter",
    "views",
    "views.main_window",
    "views.dashboard_view",
    "views.country_view",
    "views.search_view",
    "views.export_view",
]


# ── 3. Binaries extra (normalmente vacío) ────────────────────
binaries = []


# ── 4. Archivos a excluir del bundle (reduce tamaño) ─────────
excludes = [
    "pytest",
    "unittest",
    "email",
    "http",
    "urllib",
    "xml.etree.ElementTree",   # lxml la reemplaza
    "numpy",                   # no se usa en este proyecto
    "PIL",                     # no se usa
    "matplotlib",
]


# ══════════════════════════════════════════════════════════════
#  BLOQUE Analysis — el corazón del spec
# ══════════════════════════════════════════════════════════════

a = Analysis(                                          # noqa: F821
    scripts   = [os.path.join(SPEC_DIR, "main.py")],  # punto de entrada
    pathex    = [SPEC_DIR],                            # rutas de búsqueda
    binaries  = binaries,
    datas     = datas,
    hiddenimports    = hidden_imports,
    hookspath        = [],
    hooksconfig      = {},
    runtime_hooks    = [],
    excludes         = excludes,
    win_no_prefer_redirects = False,
    win_private_assemblies  = False,
    cipher    = None,
    noarchive = False,
)

# ── PYZ: archivo comprimido con todos los módulos .py ────────
pyz = PYZ(a.pure, a.zipped_data, cipher=None)        # noqa: F821


# ══════════════════════════════════════════════════════════════
#  EXE — el ejecutable en sí
# ══════════════════════════════════════════════════════════════

exe = EXE(                                             # noqa: F821
    pyz,
    a.scripts,
    [],
    exclude_binaries = True,   # True = modo onedir (los .dll van aparte)
    name    = "AlbumMind",
    debug   = False,           # True añade logs de PyInstaller al arrancar
    bootloader_ignore_signals = False,
    strip   = False,
    upx     = True,            # comprime binarios (reduce ~30% el tamaño)
    console = False,           # False = sin ventana de consola (windowed)
    disable_windowed_traceback = False,
    target_arch = None,        # None = arquitectura del sistema actual
    codesign_identity  = None,
    entitlements_file  = None,
    # ── Icono de la app ──────────────────────────────────────
    # Descomenta y ajusta la ruta cuando tengas un .ico / .icns:
    # icon = os.path.join(SPEC_DIR, "assets", "albumind.ico"),   # Windows
    # icon = os.path.join(SPEC_DIR, "assets", "albumind.icns"),  # macOS
)


# ══════════════════════════════════════════════════════════════
#  COLLECT — reúne exe + dlls + datas en dist/AlbumMind/
# ══════════════════════════════════════════════════════════════

coll = COLLECT(                                        # noqa: F821
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip  = False,
    upx    = True,
    upx_exclude = [],
    name   = "AlbumMind",   # → carpeta dist/AlbumMind/
)
