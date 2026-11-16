from datetime import datetime, time, timedelta
from helpers import get_room_id_from_user
from validators import valid_str


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