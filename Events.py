class Event():
    def __init__(self):
        # TO DO
        self.venue = None
        self.tickets = None
        self.startDate = None
        self.endDate = None
        self.description = None

    def setVenue(self, venue):
        self.venue = venue

    def getVenue(self):
        return self.venue

    def setTickets(self, tickets):
        self.tickets = tickets

    def getTickets(self):
        return self.tickets

    def setStartDate(self, startDate):
        self.startDate = startDate

    def getStartDate(self):
        return self.startDate

    def setEndDate(self, endDate):
        self.endDate = endDate

    def getEndDate(self):
        return self.endDate

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description
    
    def __str__(self):
        return f"Venue: {self.venue}, Start: {self.startDate}, End: {self.endDate}, Desc: {self.description}"

