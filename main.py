from rooms import show_all_rooms,search_room,add_room,update_room,activation
from json_functions import load_rooms
from validators import valid_str

def rooms_menu():
    print("""
    ================================
            ROOMS MENU
    ================================

    1. Show all rooms
    2. Search for a room by ID
    3. Adding a new room
    4. Update existing room details
    5. Activating or deactivating a room
    6. Return to the main menu
    """)

def room_main():
    active = True
    while  active:
        rooms = load_rooms()
        rooms_menu()
        choice = valid_str('Choose an option: ')
        match choice:
            case '1':
                show_all_rooms(rooms)
            case '2':
                search_room(rooms)
            case '3':
                add_room(rooms)
            case '4':
                update_room(rooms)
            case '5':
                activation(rooms)
            case '6':
                active = False
            case _:
                print('Invalid option.')
                                                           
def bookings_menu():
    print("""
    ================================
           BOOKINGS MENU
    ================================

    1. Create a new booking
    2. Show all bookings
    3. Search for a booking by ID
    4. Show bookings by customer
    5. Show bookings by date
    6. Update existing booking
    7. Cancel a booking
    8. Return to the main menu
    """)


def booking_main():
    active = True
    while active:
        rooms = load_rooms()
        bookings = load_bookings()
        bookings_menu()
        choice = valid_str('Choose an option: ')
        match choice:
            case '1':
                new_booking(bookings, rooms)
            case '2':
                show_all_bookings(bookings)
            case '3':
                search_booking(bookings)
            case '4':
                show_customer_bookings(bookings)
            case '5':
                show_bookings_by_date(bookings)
            case '6':
                update_booking(bookings, rooms)
            case '7':
                cancel_booking(bookings)
            case '8':
                active = False
            case _:
                print('Invalid option.')


def main_menu():
    print("""
    ================================
         ESCAPE ZONE MAIN MENU
    ================================

    1. Rooms management
    2. Bookings management
    3. Exit
    """)


def main():
    active = True
    while active:
        main_menu()
        choice = valid_str('Choose an option: ')
        match choice:
            case '1':
                room_main()
            case '2':
                booking_main()
            case '3':
                active = False
            case _:
                print('Invalid option.')


if __name__ == "__main__":
    main()
