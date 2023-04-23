import unittest
from infection_time import Hotel


class TestHotel(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel(3, 5)

    def test_minimum_infection_time(self):
        # test case from the prompt
        infection_info = [[2, 1, 0, 2, 1], [2, 2, 2, 2, 2], [1, 0, 0, 2, 1]]
        self.assertEqual(self.hotel.minimum_infection_time(infection_info), 1)

        # empty hotel
        infection_info = [[0] * 5 for _ in range(3)]
        self.assertEqual(self.hotel.minimum_infection_time(infection_info), 0)

        # all rooms infected
        infection_info = [[2] * 5 for _ in range(3)]
        self.assertEqual(self.hotel.minimum_infection_time(infection_info), 0)

        # no infected rooms
        infection_info = [[1] * 5 for _ in range(3)]
        self.assertEqual(self.hotel.minimum_infection_time(infection_info), -1)

        # one infected room, in a corner
        infection_info = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 2]]
        self.assertEqual(self.hotel.minimum_infection_time(infection_info), -1)

        # one infected room, in the middle
        infection_info = [[1, 1, 0, 0, 0], [1, 2, 1, 0, 0], [0, 1, 0, 0, 0]]
        self.assertEqual(self.hotel.minimum_infection_time(infection_info), 2)


if __name__ == '__main__':
    unittest.main()
