import sqlite3
import os

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH   = os.path.join(_BASE_DIR, "..", "albumind.db")

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