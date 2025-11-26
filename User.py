class User():
    def __init__(self):
        self.username = None
        self.password = None
        self.purchasedTickets = None
        self.cart = None

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_purchased_tickets(self, purchasedTickets):
        self.purchasedTickets = purchasedTickets

    def get_purchased_tickets(self):
        return self.purchasedTickets

    def set_cart(self, cart):
        self.cart = cart

    def get_cart(self):
        return self.cart