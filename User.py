class User():
    def __init__(self):
        self.username = None
        self.password = None
        self.purchasedTickets = None
        self.cart = None

    def setusername(self, username):
        self.username = username

    def getusername(self):
        return self.username

    def setpassword(self, password):
        self.password = password

    def getpassword(self):
        return self.password

    def setPurchasedTickets(self, purchasedTickets):
        self.purchasedTickets = purchasedTickets

    def getPurchasedTickets(self):
        return self.purchasedTickets

    def setCart(self, cart):
        self.cart = cart

    def getCart(self):
        return self.cart