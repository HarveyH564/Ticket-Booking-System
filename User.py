class User():
    def __init__(self):
        self.username = None
        self.password = None
        self.purchased_tickets = None
        self.cart = None

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_purchased_tickets(self, purchased_tickets):
        self.purchased_tickets = purchased_tickets

    def get_purchased_tickets(self):
        return self.purchased_tickets

    def set_cart(self, cart):
        self.cart = cart

    def add_to_cart(self, ticket):
        self.cart.append(ticket)

    def remove_from_cart(self, ticket):
        self.cart.remove(ticket)

    def get_cart(self):
        return self.cart