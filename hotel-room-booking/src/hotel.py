from queue import PriorityQueue
from enum import Enum
from src.room import Room, RoomStatus


class RoomTransitions(Enum):
    CHECK_IN = 1
    CHECK_OUT = 2
    CLEAN = 3
    OUT_OF_SERVICE = 4
    REPAIRED = 5
    AVAILABLE_ROOM = 6
    ROOMS_WITH_STATUS = 7


class Hotel:
    def __init__(self, floors, rooms_per_floor):
        self.floors = floors
        self.rooms_per_floor = rooms_per_floor
        self.rooms_map = {}
        self.available_rooms = PriorityQueue()
        self.__initialize_rooms__()

    def __initialize_rooms__(self):
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        req_chars = alphabets[0:int(self.rooms_per_floor)]
        priority = 1
        for i in range(1, int(self.floors) + 1):
            for j in range(int(self.rooms_per_floor)):
                alphabet = req_chars[-(j + 1)] if i % 2 == 0 else req_chars[j]
                room = Room(i, alphabet, priority)
                self.rooms_map.update({f"{i}{alphabet}": room})
                self.available_rooms.put((priority, room))
                priority += 1

    def __get_nearest_available_room__(self):
        if self.available_rooms.empty():
            raise Exception("No room available for checkout")
        return self.available_rooms.get()

    def check_in(self, guest_name=None):
        room = self.__get_nearest_available_room__()
        room.guest = guest_name if guest_name else "UNKNOWN_GUEST"
        print(f"Assigning room {room.room_number} to guest {room.guest}")
        room.room_status = RoomStatus.OCCUPIED
        return room

    def check_out(self, room_number):
        room = self.rooms_map.get(room_number)
        if room.room_status == RoomStatus.OCCUPIED:
            print(f"Checkout room {room.room_number} from guest {room.guest}")
            room.room_status = RoomStatus.VACANT
        else:
            raise Exception(f"Only Occupied rooms can be mark as check out, "
                            f"room status for room {room.room_number} is {room.room_status}")
        return room

    def mark_room_cleaned(self, room_number):
        room = self.rooms_map.get(room_number)
        if room.room_status == RoomStatus.VACANT:
            print(f"Checkout room {room.room_number} from guest {room.guest}")
            room.room_status = RoomStatus.AVAILABLE
        else:
            raise Exception(f"Only Vacant rooms can be mark as cleaned, "
                            f"room status for room {room.room_number} is {room.room_status}")
        return room

    def mark_room_out_of_service(self, room_number):
        room = self.rooms_map.get(room_number)
        if room.room_status == RoomStatus.VACANT:
            print(f"Checkout room {room.room_number} from guest {room.guest}")
            room.room_status = RoomStatus.REPAIR
        else:
            raise Exception(f"Only Vacant rooms can be mark as out of service, "
                            f"room status for room {room.room_number} is {room.room_status}")
        return room

    def mark_room_repaired(self, room_number):
        room = self.rooms_map.get(room_number)
        if room.room_status == RoomStatus.REPAIR:
            print(f"Checkout room {room.room_number} from guest {room.guest}")
            room.room_status = RoomStatus.VACANT
        else:
            raise Exception(f"Only Repaired rooms can be mark as repaired, "
                            f"room status for room {room.room_number} is {room.room_status}")
        return room

    def list_available_rooms(self):
        print(self.available_rooms)
        return self.available_rooms

    def get_room_with_status(self, status):
        print(self.rooms_map)
        rooms = [room for _, room in self.rooms_map.items() if room.room_status == status]
        print(f"Rooms with status {status} : {rooms}")
        return rooms
