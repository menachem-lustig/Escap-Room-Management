from pathlib import Path
import json

rooms_file = Path(__file__).parent / "rooms.json"
booking_file = Path(__file__).parent / 'bookings.json'

def load_rooms():
    with open(rooms_file, "r", encoding="utf-8") as file:
        rooms = json.load(file)                    
    return rooms

def save_rooms (rooms):
    with open(rooms_file, "w", encoding="utf-8") as file:
        json.dump(rooms, file, indent=2, ensure_ascii=False)


def load_bookings():
    with open(booking_file, "r", encoding="utf-8") as file:
        bookings = json.load(file)                    
    return bookings

def save_bookings (bookings):
    with open(booking_file, "w", encoding="utf-8") as file:
        json.dump(bookings, file, indent=2, ensure_ascii=False)
    



