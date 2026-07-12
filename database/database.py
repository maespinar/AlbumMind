import os
import sqlite3
from pathlib import Path

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def obtener_ruta_bd() -> str:
    ruta_personalizada = os.getenv("ALBUMIND_DB_PATH")
    if ruta_personalizada:
        return ruta_personalizada

    appdata_local = os.getenv("LOCALAPPDATA")
    if appdata_local:
        ruta_carpeta = Path(appdata_local) / "AlbumMind"
    else:
        ruta_carpeta = Path.home() / "AppData" / "Local" / "AlbumMind"

    ruta_carpeta.mkdir(parents=True, exist_ok=True)
    return str(ruta_carpeta / "albumind.db")


DB_PATH = obtener_ruta_bd()

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    schema_path = os.path.join(_BASE_DIR, "schema.sql")
    with get_connection() as conn:
        with open(schema_path, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
