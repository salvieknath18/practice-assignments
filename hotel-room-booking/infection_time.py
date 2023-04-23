from collections import deque


class Hotel:

    def __init__(self, floors, rooms_per_floor):
        self.floors = floors
        self.rooms_per_floor = rooms_per_floor
        self.infected = deque([])

    def minimum_infection_time(self, infection_info):
        for i in range(self.floors):
            for j in range(self.rooms_per_floor):
                if infection_info[i][j] == 2:
                    self.infected.append((i, j, 0))
        max_time = 0

        while self.infected:
            i, j, time = self.infected.popleft()
            max_time = max(max_time, time)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < self.floors and 0 <= nj < self.rooms_per_floor and infection_info[ni][nj] == 1:
                    infection_info[ni][nj] = 2
                    self.infected.append((ni, nj, time+1))

        if any(1 in row for row in infection_info):
            return -1
        else:
            return max_time


if __name__ == "__main__":
    retry = 1
    while retry < 3:
        inp = input("Enter value floors and rooms per floor, separated with space")
        try:
            m, n = inp.split(" ")
            if 0 > int(m) > 1000 and 0 > int(n) > 1000:
                raise Exception("Invalid Input")
        except Exception as E:
            print("Entered wrong values, please Enter value of floors and rooms per floor, "
                  "value between 1 to 1000, separated with space")
            continue
        hotel = Hotel(int(m), int(n))
        inp = input("""
        enter infection info in hotel room 
        eg. if floors = 3 and rooms per floor =  4 then enter
        [1,2,0,1] [2,1,0,2] [1,1,1,1]
        """)
        hotel_infection_info = [[int(val) for val in floor[1:-1].split(",")] for floor in inp.split(" ")]
        # TO-DO : Can do more extensive check and validation on input provided for infection in hotel.
        # Adding this as a part for future improvements'
        # hotel_infection_info = [[2, 1, 0, 2, 1], [1, 1, 1, 1, 1], [1, 0, 0, 2, 1]]
        if len(hotel_infection_info) == int(m) and len(hotel_infection_info[0]) == int(n):
            print(f"Minimum Infection time is {hotel.minimum_infection_time(hotel_infection_info)}")
        else:
            raise Exception("Inadequate information")
