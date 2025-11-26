class Venue():
    def __init__(self, seats):
        self.seats = seats
        self.location = ""

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
            rowList = ""
            for seat in row:
                rowList += str(seat)
            print(rowList)
