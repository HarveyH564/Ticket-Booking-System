class Venue:
    def __init__(self):
        self.location = None
        self.seats = None

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def setSeats(self, seats):
        self.seats = seats

    def getSeats(self):
        return self.seats