from db import init_db
from rooms import add_room, get_rooms
from booking import make_booking, get_bookings
from db import get_connection

# Functie pentru a gasi ID-ul camerei dupa numar
def get_room_id_by_number(room_number):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM rooms WHERE number = ?", (room_number,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def menu():
    while True:
        print("\n--- HOTEL MANAGEMENT ---")
        print("1. Adauga camera")
        print("2. Vezi camere")
        print("3. Fa rezervare")
        print("4. Vezi rezervari")
        print("0. Iesire")

        choice = input("Alege: ")

        if choice == "1":
            number = input("Numar camera: ")
            price = float(input("Pret: "))
            add_room(number, price)
            print(f"Camera {number} adaugata!\n")

        elif choice == "2":
            print("Numar | Pret | Status")
            for r in get_rooms():
                status = "Libera" if r[3] == 1 else "Ocupata"
                print(f"{r[1]} | {r[2]} | {status}")

        elif choice == "3":
            name = input("Nume client: ")
            room_number = input("Numar camera: ")
            room_id = get_room_id_by_number(room_number)
            if room_id:
                make_booking(name, room_id)
            else:
                print("Camera nu exista!")

        elif choice == "4":
            print("ID | Client | Camera")
            for b in get_bookings():
                print(f"{b[0]} | {b[1]} | {b[2]}")

        elif choice == "0":
            break
        else:
            print("Optiune invalida!")

if __name__ == "__main__":
    init_db()
    menu()

