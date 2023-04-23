from enum import Enum

from src.hotel import Hotel


class RoomTransitions(Enum):
    CHECK_IN = 1
    CHECK_OUT = 2
    CLEAN = 3
    OUT_OF_SERVICE = 4
    REPAIRED = 5
    AVAILABLE_ROOM = 6
    ROOMS_WITH_STATUS = 7


def room_transition(option, hotel_obj):
    if option == RoomTransitions.CHECK_IN.value:
        guest = input("Enter guest Name")
        if guest:
            hotel_obj.check_in(guest)
        else:
            hotel_obj.check_in()
    elif option == RoomTransitions.AVAILABLE_ROOM.value:
        hotel_obj.list_available_rooms()
    elif option == RoomTransitions.ROOMS_WITH_STATUS.value:
        i = 0
        while i < 3:
            status = input("""
            Please select one from the following status
            1. Available
            2. Occupied
            3. Vacant
            4. Repaired
            0. Exit
            """)
            if status in "1234" and len(status) == 1:
                hotel_obj.get_room_with_status(int(status))
                break
            else:
                print("Enter Valid input or enter 0 for exit")
                i += 1
            if opt == '0':
                break
    else:
        room_number = input("Please enter room number")
        if option == RoomTransitions.CHECK_OUT.value:
            hotel_obj.check_out(room_number)
        if option == RoomTransitions.CLEAN.value:
            hotel_obj.mark_room_cleaned(room_number)
        if option == RoomTransitions.OUT_OF_SERVICE.value:
            hotel_obj.mark_room_out_of_service(room_number)
        if option == RoomTransitions.REPAIRED.value:
            hotel_obj.mark_room_repaired(room_number)


if __name__ == '__main__':
    hotel = Hotel(floors=4, rooms_per_floor=5)
    while 1:
        print("""
        please select
        1. Book room (check in)
        2. Checkout room
        3. Mark room clean
        4. Mark room out of service 
        5. Mark room repaired
        6. Check available room
        7. Check room with status 
        0. Exit
        """)
        opt = input()
        if opt in "1234567" and len(opt) == 1:
            try:
                room_transition(int(opt), hotel)
            except Exception as E:
                print(f"Error: {E}")
        else:
            print("Enter Valid input or enter 0 for exit")

        if opt == '0':
            break
