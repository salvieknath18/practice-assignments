from enum import Enum


class RoomStatus(Enum):
    AVAILABLE = 1
    OCCUPIED = 2
    VACANT = 3
    REPAIR = 4


class Room:

    def __init__(self, floor, letter, room_priority):
        self.floor = floor
        self.alphabet = letter
        self.room_number = f"{self.floor}{self.alphabet}"
        self.priority = room_priority
        self._room_status = RoomStatus.AVAILABLE
        self.guest = ""

    @property
    def room_status(self):
        return self._room_status

    @room_status.setter
    def room_status(self, value):
        if value in RoomStatus:
            self._room_status = value
        else:
            raise Exception("Not valid state")

    def __repr__(self):
        return f"{self.priority}/{self.room_number}/{self.room_status.value}"
