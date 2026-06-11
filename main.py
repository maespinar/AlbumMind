import os
import sys
import sqlite3

def resource_path(relative: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)

def _db_path() -> str:
    if getattr(sys, "frozen", False):
        return os.path.join(os.path.dirname(sys.executable), "albumind.db")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "albumind.db")

def init_database() -> None:
    db     = _db_path()
    schema = resource_path(os.path.join("database", "schema.sql"))
    seed   = resource_path(os.path.join("database", "seed_data.sql"))
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