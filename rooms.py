from db import get_connection

def add_room(number, price):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO rooms VALUES (NULL, ?, ?, 1)",
        (number, price)
    )
    conn.commit()
    conn.close()

def get_rooms():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM rooms")
    rooms = c.fetchall()
    conn.close()
    return rooms
