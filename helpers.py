from validators import valid_str


def get_room_by_id(rooms,room_id):
     for room in rooms:
            if room['room_id'] == room_id:
                return room


   
            

def get_room_id_from_user(rooms):
    found = False
    while not found:
        room_id = valid_str("Enter room id: ")
        found = get_room_by_id(rooms,room_id)
        if not found:
            print('Room not found , try again')
    return found

        
    

def uniq_room_id(rooms):
    new_id = max(int(room['room_id'][1:]) for room in rooms) + 1
    str_id = str(new_id)
    if len(str_id) < 3:
        for _ in range(3-len(str_id)):
            str_id = '0'+ str_id
    return 'R' + str_id


def uniq_booking_id(bookings):
    new_id = max(int(booking['booking_id'][1:]) for booking in bookings) + 1
    str_id = str(new_id)
    if len(str_id) < 3:
        for _ in range(3-len(str_id)):
            str_id = '0'+ str_id
    return 'B' + str_id

def get_booking_by_id(bookings, booking_id):
    for booking in bookings:
        if booking['booking_id'] == booking_id:
            return booking


def get_booking_id_from_user(bookings):
    found = False
    while not found:
        booking_id = valid_str("Enter booking id: ")
        found = get_booking_by_id(bookings, booking_id)
        if not found:
            print('Booking not found, try again.')
    return found