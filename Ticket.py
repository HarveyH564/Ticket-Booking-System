class Ticket():
    def __init__(self):
        # TO DO
        self.id = None
        self.purchased = False
        self.userID = None
        self.price = None
        self.type = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_purchased(self, purchased):
        self.purchased = purchased

    def get_purchased(self):
        return self.purchased

    def set_user_id(self, userID):
        self.userID = userID

    def get_user_id(self):
        return self.userID

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type