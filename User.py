class User():
    def __init__(self):
        self.userID = None
        self.userPassword = None
        self.purchasedTickets = None

    def setUserID(self, userID):
        self.userID = userID

    def getUserID(self):
        return self.userID

    def setUserPassword(self, userPassword):
        self.userPassword = userPassword

    def getUserPassword(self):
        return self.userPassword

    def setPurchasedTickets(self, purchasedTickets):
        self.purchasedTickets = purchasedTickets

    def getPurchasedTickets(self):
        return self.purchasedTickets