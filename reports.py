from datetime import datetime, time, timedelta
from helpers import get_room_id_from_user,get_room_by_id
from validators import valid_str


def active_bookings(bookings):
    print(f'total active bookings: {len([booking for booking in bookings if booking['status'] == "Active"])}')
            
def canceled_bookings(bookings):
     print(f'total cancelled bookings: {len([booking for booking in bookings if booking['status'] == "Cancelled"])}')

def total_revenues(bookings):
    active = [booking for booking in bookings if booking['status'] == 'Active']
    if not active:
        print('No active bookings')
        return
    print( f'total_revenues: {sum(booking['total_price'] for booking in active)}')


def total_cancellation_fee(bookings):
    canceled_bookings = [booking for booking in bookings if booking['status'] == 'Cancelled']
    if not canceled_bookings:
        print('No canceled booking')
        return
    print(f'total cancellation_fee: {sum(booking["cancellation_fee"] for booking in canceled_bookings )}')


def most_popular_room(bookings,rooms): 
    bookings_rooms = {}
    for booking in bookings:
        if booking['status'] == 'Active':
            if booking['room_id'] not in bookings_rooms:
                bookings_rooms[booking['room_id']] = 1
            else:
                bookings_rooms[booking['room_id']] += 1
    if not bookings_rooms:
        print('No active bookings ')
        return
    popular_room_id = max(bookings_rooms,key = bookings_rooms.get)
    room = get_room_by_id(rooms,popular_room_id)
    print(f'most popular room:  {room}')

def bookings_by_room(bookings):
    if not bookings:
        print('No bookings')
        return
    bookings_rooms = {}
    for booking in bookings:
        if booking['room_id'] not in bookings_rooms:
            bookings_rooms[booking['room_id']] = 1
        else:
            bookings_rooms[booking['room_id']] += 1
    for room,bookings in bookings_rooms.items():
        print(f'room id: {room}, number of bookings: {bookings}')
    



def room_occupancy(rooms, bookings):
    room = get_room_id_from_user(rooms)
    valid = False
    while not valid:
        date_str = valid_str('Enter date (YYYY-MM-DD): ')
        try:
            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            valid = True
        except ValueError:
            print('Invalid format. Please use YYYY-MM-DD.')

    closing_datetime = datetime.combine(selected_date, time(22, 0))
    occupied_minutes = 0

    for booking in bookings:
        if booking['room_id'] == room['room_id'] and booking['booking_date'] == date_str and booking['status'] == 'Active':
            start_dt = datetime.strptime(f"{booking['booking_date']} {booking['start_time']}", "%Y-%m-%d %H:%M")
            end_dt = start_dt + timedelta(minutes=room['duration'] + 15)
            actual_end = min(end_dt, closing_datetime)
            occupied_minutes += (actual_end - start_dt).total_seconds() / 60

    occupancy_percent = round((occupied_minutes / 720) * 100, 2)
    print(f"Room {room['name']} ({room['room_id']}) occupancy on {date_str}: {occupancy_percent}%")