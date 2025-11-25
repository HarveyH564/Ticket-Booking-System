class Ticket():
    def __init__(self):
        # TO DO
        self.id = None
        self.purchased = False
        self.userID = None
        self.price = None
        self.type = None

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id

    def setPurchased(self, purchased):
        self.purchased = purchased

    def getPurchased(self):
        return self.purchased

    def setUserID(self, userID):
        self.userID = userID

    def getUserID(self):
        return self.userID

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type