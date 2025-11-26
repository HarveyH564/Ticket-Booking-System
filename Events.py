import os

class Event():
    def __init__(self):
        # TO DO
        self.venue = None
        self.tickets = None
        self.startDate = None
        self.endDate = None
        self.description = None

    def set_venue(self, venue):
        self.venue = venue

    def get_venue(self):
        return self.venue

    def set_tickets(self, tickets):
        self.tickets = tickets

    def get_tickets(self):
        return self.tickets

    def set_start_date(self, startDate):
        self.startDate = startDate

    def get_start_date(self):
        return self.startDate

    def set_end_date(self, endDate):
        self.endDate = endDate

    def get_end_date(self):
        return self.endDate

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
    
    def __str__(self):
        return f"Venue: {self.venue}, Start: {self.startDate}, End: {self.endDate}, Desc: {self.description}"

    def save_event(self):
        if not os.path.isdir("events"):
            os.mkdir("events")