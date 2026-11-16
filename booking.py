from helpers import uniq_booking_id,get_room_id_from_user,get_booking_id_from_user,get_room_by_id
from validators import valid_str,valid_date,valid_time,valid_number_players,free_time
from datetime import datetime,date
from json_functions import save_bookings

def active_room(rooms):
    valid_room = False
    while not valid_room:
        room = get_room_id_from_user(rooms)
        if room['is_active']:
            return room
        print('The room is inactive.')

def calculate_price(room,players,date_str):
    base_price = room['price_per_player'] * players
    if players < 5:
        discount = 0
    elif players < 7:
        discount = 10
    else:
        discount = 15
    after_discount = base_price -(base_price * discount / 100)
    booking_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    if booking_date.weekday() in (4,5):
        after_discount += (after_discount * 15 / 100)
    return round(after_discount,2)

    

def new_booking(bookings,rooms):
    booking_id = uniq_booking_id(bookings)
    customer_name = valid_str('Enter customer name: ')
    room = active_room(rooms)
    players = valid_number_players(room)
    available = False
    while not available:
        selected_date = valid_date()
        date_str,time_str = valid_time(selected_date,room)
        if free_time(room,bookings,date_str,time_str):
            available = True
            total_price = calculate_price(room,players,date_str)
            booking = {
            "booking_id": booking_id,
            "customer_name": customer_name,
            "room_id": room['room_id'],
            "booking_date": date_str,
            "start_time": time_str,
            "players": players,
            "total_price": total_price,
            "status": "Active",
            "cancellation_fee": 0.0}
            bookings.append(booking)
            save_bookings(bookings)
            print('The booking saved successfully')
        else:
            print('The room is occupied at this time, try another time.')


def show_all_bookings(bookings):
    for booking in bookings:
        print(booking)


def search_booking(bookings):
    print(get_booking_id_from_user(bookings))


def show_customer_bookings(bookings):
    name = valid_str('Enter customer name: ').lower()
    found = False
    for booking in bookings:
        if booking['customer_name'].lower() == name:
            print(booking)
            found = True
    if not found:
        print('No bookings found for this customer.')

def show_bookings_by_date(bookings):
    date_str = valid_str('Enter date (YYYY-MM-DD): ')
    found = False
    for booking in bookings:
        if booking['booking_date'] == date_str:
            print(booking)
            found = True
    if not found:
        print('No bookings found for this date.')

def update_booking(bookings, rooms):
    booking = get_booking_id_from_user(bookings)
    if booking['status'] != 'Active':
        print('Only active bookings can be updated.')
        return
    room = get_room_by_id(rooms, booking['room_id'])
    if not room or not room['is_active']:
        print('The room is inactive.')
        return
    choice = valid_str('What would you like to change? (date, time, players): ').lower()
    match choice:
        case 'date':
            new_date = valid_date()
            new_date_str = new_date.strftime("%Y-%m-%d")
            existing_time = datetime.strptime(booking['start_time'], "%H:%M").time()
            if datetime.combine(new_date, existing_time) <= datetime.now():
                print('The selected time has already passed today.')
                return
            if free_time(room, bookings, new_date_str, booking['start_time'], booking['booking_id']):
                booking['booking_date'] = new_date_str
                booking['total_price'] = calculate_price(room, booking['players'], new_date_str)
                save_bookings(bookings)
                print('Booking updated successfully.')
            else:
                print('The room is occupied at this time.')
        case 'time':
            existing_date = datetime.strptime(booking['booking_date'], "%Y-%m-%d").date()
            if existing_date < date.today():
                print('Cannot change time for a past date.')
                return
            date_str, new_time_str = valid_time(existing_date, room)
            if free_time(room, bookings, date_str, new_time_str, booking['booking_id']):
                booking['start_time'] = new_time_str
                booking['total_price'] = calculate_price(room, booking['players'], date_str)
                save_bookings(bookings)
                print('Booking updated successfully.')
            else:
                print('The room is occupied at this time.')
        case 'players':
            new_players = valid_number_players(room)
            booking['players'] = new_players
            booking['total_price'] = calculate_price(room, new_players, booking['booking_date'])
            save_bookings(bookings)
            print('Booking updated successfully.')
        case _:
            print('Invalid value for change.')

def cancel_booking(bookings):
    booking = get_booking_id_from_user(bookings)
    if booking['status'] == 'Cancelled':
        print('Booking is already cancelled.')
        return
    start_datetime = datetime.strptime(f"{booking['booking_date']} {booking['start_time']}", "%Y-%m-%d %H:%M")
    now = datetime.now()
    if start_datetime <= now:
        print('Cannot cancel a booking after its start time.')
        return
    hours_left = (start_datetime - now).total_seconds() / 3600
    if hours_left > 24:
        fee_percent = 0
    elif hours_left >= 6:
        fee_percent = 25
    else:
        fee_percent = 50
    cancellation_fee = round(booking['total_price'] * fee_percent / 100, 2)
    booking['status'] = 'Cancelled'
    booking['cancellation_fee'] = cancellation_fee
    save_bookings(bookings)
    print(f'Booking cancelled. Cancellation fee: {cancellation_fee}')



   







