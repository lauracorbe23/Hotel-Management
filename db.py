import sqlite3

DB_NAME = "hotel.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    c = conn.cursor()

    # Tabel camere
    c.execute("""
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT,
        price REAL,
        available INTEGER
    )
    """)

    # Tabel rezervari
    c.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        room_id INTEGER
    )
    """)

    conn.commit()
    conn.close()
