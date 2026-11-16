from json_functions import save_rooms
from helpers import uniq_room_id,get_room_id_from_user
from validators import valid_str,valid_difficulty,valid_int,valid_min_max_plyers

def show_all_rooms(rooms):
    for room in rooms:
        print(room)

def search_room(rooms):
    print(get_room_id_from_user(rooms))
    


def add_room(rooms):
    room_id = uniq_room_id(rooms)
    name = valid_str('Enter room name: ')
    difficulty  = valid_difficulty()
    duration = valid_int('Enter the duration of the game in the room:  ')
    min_plyers,max_plyers = valid_min_max_plyers()
    price_per_player = valid_int('Enter Price per player: ')
    room = {
        "room_id": room_id,
        "name": name,
        "difficulty": difficulty,
        "duration": duration,
        "min_players": min_plyers,
        "max_players": max_plyers,
        "price_per_player":price_per_player,
        "is_active": True
    }

    rooms.append(room)
    save_rooms(rooms)
    print('The room added successfully.')

def update_room(rooms):
    room = get_room_id_from_user(rooms)
    choice = valid_str('What would you like to change?(name,difficulty,duration,min and max_plyers,price_per_plyer): ').lower()
    change = True
    match choice:
        case 'name':
            name = valid_str('Enter room name: ')
            room['name'] = name
        case 'difficulty':
            difficulty  = valid_difficulty()
            room['difficulty'] = difficulty
        case 'duration':
            duration = valid_int('Enter the duration of the game in the room:  ')
            room['duration'] = duration
        case 'min and max_plyers':
            min_plyers,max_plyers = valid_min_max_plyers()
            room['min_players'] = min_plyers
            room['max_players'] = max_plyers
        case 'price_per_plyer':
            price_per_player = valid_int('Enter Price per player: ')
            room['price_per_player'] = price_per_player
        case _:
            change = False
            print('Invalid value for change')
    if change:
        save_rooms(rooms)

        
def activation(rooms):
    room = get_room_id_from_user(rooms)
    active = valid_str('Is this an active room? 1.Yes,2.No.')
    match active:
        case '1':
            room['is_active'] = True
        case '2':
            room['is_active'] = False
        case _:
            print("choose 1 or 2.")
    save_rooms(rooms)

 







            
    





