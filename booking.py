from db import get_connection

def make_booking(name, room_id):
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT available FROM rooms WHERE id = ?", (room_id,))
    room = c.fetchone()

    if room and room[0] == 1:
        c.execute(
            "INSERT INTO bookings VALUES (NULL, ?, ?)",
            (name, room_id)
        )
        c.execute(
            "UPDATE rooms SET available = 0 WHERE id = ?",
            (room_id,)
        )
        conn.commit()
        print("Rezervare realizata!")
    else:
        print("Camera este ocupata.")

    conn.close()

def get_bookings():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT b.id, b.name, r.number
        FROM bookings b
        JOIN rooms r ON b.room_id = r.id
    """)
    data = c.fetchall()
    conn.close()
    return data
