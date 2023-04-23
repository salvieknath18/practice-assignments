import unittest
from queue import PriorityQueue
from src.room import RoomStatus
from src.hotel import Hotel


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel(floors=3, rooms_per_floor=5)

    def test_initialization(self):
        self.assertEqual(self.hotel.floors, 3)
        self.assertEqual(self.hotel.rooms_per_floor, 5)
        self.assertIsInstance(self.hotel.rooms_map, dict)
        self.assertIsInstance(self.hotel.available_rooms, PriorityQueue)
        self.assertEqual(len(self.hotel.rooms_map), 15)
        self.assertEqual(self.hotel.available_rooms.qsize(), 15)

    def test_check_in(self):
        room = self.hotel.check_in("John Doe")
        self.assertEqual(room.room_status, RoomStatus.OCCUPIED)
        self.assertEqual(room.guest, "John Doe")

    def test_check_out(self):
        room = self.hotel.check_in("Jane Smith")
        self.assertEqual(room.room_status, RoomStatus.OCCUPIED)
        self.assertEqual(room.guest, "Jane Smith")
        self.hotel.check_out(room.room_number)
        self.assertEqual(room.room_status, RoomStatus.VACANT)
        self.assertIsNone(room.guest)

    def test_mark_room_cleaned(self):
        room = self.hotel.check_in("Alice Brown")
        self.assertEqual(room.room_status, RoomStatus.OCCUPIED)
        self.hotel.check_out(room.room_number)
        self.assertEqual(room.room_status, RoomStatus.VACANT)
        self.assertIsNone(room.guest)
        self.hotel.mark_room_cleaned(room.room_number)
        self.assertEqual(room.room_status, RoomStatus.AVAILABLE)

    def test_mark_room_out_of_service(self):
        room = self.hotel.check_in("Bob Smith")
        self.assertEqual(room.room_status, RoomStatus.OCCUPIED)
        self.hotel.check_out(room.room_number)
        self.assertEqual(room.room_status, RoomStatus.VACANT)
        self.assertIsNone(room.guest)
        self.hotel.mark_room_out_of_service(room.room_number)
        self.assertEqual(room.room_status, RoomStatus.OUT_OF_SERVICE)

    def test_mark_room_repaired(self):
        room = self.hotel.check_in("Charlie Brown")
        self.assertEqual(room.room_status, RoomStatus.OCCUPIED)
        self.hotel.check_out(room.room_number)
        self.assertEqual(room.room_status, RoomStatus.VACANT)
        self.assertIsNone(room.guest)
        self.hotel.mark_room_out_of_service(room.room_number)
        self.assertEqual(room.room_status, RoomStatus.OUT_OF_SERVICE)
        self.hotel.mark_room_repaired(room.room_number)
        self.assertEqual(room.room_status, RoomStatus.VACANT)

    def test_list_available_rooms(self):
        self.hotel.check_in("David Brown")
        self.hotel.check_in("Elizabeth Smith")
        available_rooms = self.hotel.list_available_rooms()
        self.assertEqual(len(available_rooms), 13)

    def test_get_room_with_status(self):
        self.hotel.check_in("Frank Brown")
        self.hotel.check_out("1A")
        self.hotel.mark_room_out_of_service("1A")
        self.hotel.mark_room_repaired("1A")
        rooms = self.hotel.get_room_with_status(RoomStatus.AVAILABLE.value)
        self.assertEqual(len(rooms), 14)


if __name__ == '__main__':
    unittest.main()

