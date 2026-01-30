import sqlite3
import json

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        report TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_user(data: dict) -> int:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "INSERT INTO users (data) VALUES (?)",
        (json.dumps(data),)
    )

    user_id = c.lastrowid
    conn.commit()
    conn.close()

    return user_id


def save_report(user_id: int, report: dict):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "UPDATE users SET report=? WHERE id=?",
        (json.dumps(report), user_id)
    )

    conn.commit()
    conn.close()


def fetch_report(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT report FROM users WHERE id=?", (user_id,))
    row = c.fetchone()
    conn.close()

    if row and row[0]:
        return json.loads(row[0])
    return {}
