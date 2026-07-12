import os
import shutil
import sys
import sqlite3
from pathlib import Path

from database.database import obtener_ruta_bd

def resource_path(relative: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)

def _legacy_db_paths() -> list[Path]:
    if getattr(sys, "frozen", False):
        return [Path(sys.executable).resolve().parent / "albumind.db"]
    return [Path(__file__).resolve().parent / "albumind.db"]

def _migrate_legacy_database(db: str) -> None:
    target = Path(db)
    if target.exists():
        return

    for legacy_db in _legacy_db_paths():
        if legacy_db.exists() and legacy_db.resolve() != target.resolve():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(legacy_db, target)
            return

def init_database() -> None:
    db     = obtener_ruta_bd()
    schema = resource_path(os.path.join("database", "schema.sql"))
    seed   = resource_path(os.path.join("database", "seed_data.sql"))
    _migrate_legacy_database(db)
    conn = sqlite3.connect(db)
    conn.execute("PRAGMA foreign_keys = ON")
    with open(schema, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    count = conn.execute("SELECT COUNT(*) FROM PAIS").fetchone()[0]
    if count == 0:
        with open(seed, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
    conn.close()
    import database.database as db_module
    db_module.DB_PATH = db

def main() -> None:
    init_database()
    from views.main_window import MainWindow
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
