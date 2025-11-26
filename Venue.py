class Venue():
    def __init__(self, seats):
        self.seats = seats
        self.location = ""

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def setSeats(self, seats):
        self.seats = seats

    def getSeats(self):
        return self.seats

    def printSeats(self):
        for row in self.seats:
            rowList = ""
            for seat in row:
                rowList += str(seat)
            print(rowList)


#x = Venue([[["standard"], ["standard"], ["standard"]], [["standard"],["standard"], ["vip"], ["standard"]]])
#x.printSeats()