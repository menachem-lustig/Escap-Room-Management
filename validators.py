
from datetime import datetime,time,date,timedelta


def valid_str(text):
    valid = False
    while not valid:
        user = input(text).strip()
        if user:
            valid = user
        else:
            print('Cannot be empty.')
    return valid


def valid_difficulty():
    valid =  False
    while not valid:
        difficulty = valid_str('Enter difficulty (Easy,Medium,hard): ').capitalize()
        if difficulty in ['Easy','Medium','Hard']:
            valid = difficulty
        else:
            print('Difficulty must be Easy Medium or hard.')
    return valid

def valid_int(text):
    valid = False
    while not valid:
        try:
            num = int(input(text))
            if num > 0:
                valid = num
            else:
                print('The number must be greater than 0.')
        except ValueError:
            print('Must be a number.')
    return valid

def valid_min_max_plyers():
    valid = False
    while not valid:
        min_plyers = valid_int('Enter minimum number of players: ')
        max_plyers= valid_int('Enter maximum number of players: ')
        if max_plyers >= min_plyers:
            valid = min_plyers,max_plyers
        else:
            print("Maximum players must be greater than minimum.")
    return valid

def valid_date():
    valid = False
    while not valid:
        user_input = input('Select a date for the game (YYYY-MM-DD): ')
        try:
            parsed_date = datetime.strptime(user_input, "%Y-%m-%d").date()
            if parsed_date >= date.today():
                valid = parsed_date
            else:
                print('Date cannot be in the past.')
        except ValueError:
            print('Invalid format. Please use YYYY-MM-DD.')
    return valid


def valid_time(selected_date,room):
    valid = False
    while not valid:
        user = input('Select a time for the game (HH:MM): ')
        try:
            user_time = datetime.strptime(user, "%H:%M").time()
            if user_time < time(10,0):
                print('Operating hours are between 10:00 and 22:00.')
                continue
            full_datetime = datetime.combine(selected_date, user_time)
            end_datetime = full_datetime + timedelta(minutes=room['duration'])
            closing_datetime = datetime.combine(selected_date,time(22,0))
            if end_datetime > closing_datetime:
                print('Operating hours are between 10:00 and 22:00.')
                continue
            if full_datetime > datetime.now():
                valid = (selected_date.strftime("%Y-%m-%d"), user_time.strftime("%H:%M"))
            else:
                print('The selected time has already passed today. Please choose a future time.')
        except ValueError:
            print('Invalid format. Please use HH:MM.')
    return valid


def free_time(room,bookings,date_str,time_str,ignore_booking_id=None):
    start_new_booking =  datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
    end_new_booking = start_new_booking + timedelta(minutes=room['duration'] + 15)
    available = True
    for booking in bookings:
        if room['room_id'] == booking['room_id'] and booking['status'] == 'Active' and booking['booking_id'] != ignore_booking_id:
            start_booking = datetime.strptime(f'{booking['booking_date']} {booking['start_time']}', "%Y-%m-%d %H:%M")
            end_booking = start_booking + timedelta(minutes = room['duration'] + 15)
            if start_new_booking < end_booking and end_new_booking > start_booking:
                available = False
    return available


def valid_number_players(room):
    valid = False
    while not valid:
        players = valid_int('Enter number of players: ')
        if room['min_players'] <= players <= room['max_players']:
            return players
        print(f'The number of players must be between {room['min_players']} and {room['max_players']}.')