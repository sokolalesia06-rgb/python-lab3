import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL
)
""")

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def add_user(login, password, full_name):
    hashed_password = hash_password(password)
    cursor.execute(
        "INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)",
        (login, hashed_password, full_name)
    )
    conn.commit()

add_user("student24", "mypassword123", "Сокол Алеся Ігорівна")

conn.close()
