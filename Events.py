import json
import os
import datetime

def get_all_events():
    # TO DO
    if not os.path.isdir("events"):
        return "No events exist please create one"
    else:
        event_list = []
        for file in os.listdir("events"):
            event_list.append((os.path.basename(file).removesuffix(".json")))
        return event_list

def get_available_events():
    if not os.path.isdir("events"):
        # TO CHANGE user cant make events
        return ["No events exist please create one"]
    else:
        event_list = []
        for file in os.listdir("events"):
            f = open("events/" + file, "r")
            file_info = json.loads(f.read())
            if datetime.datetime.strptime(file_info["Start date"], "%d-%m-%Y").date() >= datetime.date.today() and file_info["Tickets"] != None:
                event_list.append(file_info["Event name"])
            f.close()
        # if there are events but none upcoming
        return event_list

def show_available_events():
    # Available events
    print("\n=== Available Events ===")
    print("1. Rock concert")
    print("2. Pop concert")
    print("3. International band performance")
    print("4. Local band performance")
    print("=========================\n")

class Event():
    def __init__(self):
        # TO DO
        self.event_name = None
        self.venue = None
        self.tickets = None
        self.start_date = None
        self.end_date = None
        self.description = None

    def set_event_name(self, event_name):
        self.event_name = event_name

    def get_event_name(self):
        return self.event_name

    def set_venue(self, venue):
        self.venue = venue

    def get_venue(self):
        return self.venue

    def set_tickets(self, tickets):
        self.tickets = tickets

    def get_tickets(self):
        return self.tickets

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_start_date(self):
        return self.start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_end_date(self):
        return self.end_date

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
    
    def __str__(self):
        return f"Venue: {self.venue}, Start: {self.start_date}, End: {self.end_date}, Desc: {self.description}"

    def save_event(self):
        if not os.path.isdir("events"):
            os.mkdir("events")
        else:
            if os.path.exists("events/" + self.event_name.replace(" ", "_").lower()):
                print("Event already exists, update or delete it")
            else:
                event_file = open("events/" + self.event_name.replace(" ", "_").lower() + ".json", "w")
                event_info = {
                    "Event name": self.event_name,
                    "Venue": self.venue.get_location(),
                    "Tickets": self.tickets,
                    "Start date": self.start_date,
                    "End date": self.end_date,
                    "Description": self.description
                }
                json_input = json.dumps(event_info)
                event_file.write(json_input)
                event_file.close()
                print("Event saved successfully")