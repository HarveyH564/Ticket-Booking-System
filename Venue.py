import ast

class Venue():
    def __init__(self):
        self.seats = None
        self.location = None

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_seats(self, seats):
        self.seats = seats

    def get_seats(self):
        return self.seats

    def print_seats(self):
        for row in self.seats:
            row_list = ""
            for seat in row:
                row_list += str(seat)
            print(row_list)

    def __str__(self):
        return self.location