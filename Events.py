import json
import os
import Users
import datetime
import sqlite3


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

# testing with a events list can be changed later
event1 = Event()
# Using direct attributes instead of setters to avoid AttributeError
event1.venue = "Club21"
event1.start_date = "12-12-2012"
event1.end_date = "13-12-2012"
event1.description = "Student night"
event1.tickets = 20

events = [event1]

def create_event(event_name, venue_name, tickets, start_date, end_date, description):
    if not os.path.isdir("events"):
        os.mkdir("events")
    else:
        if os.path.exists("events/" + event_name.replace(" ", "_").lower()):
            print("Event already exists, update or delete it")
        else:
            event_file = open("events/" + event_name.replace(" ", "_").lower() + ".json", "w")
            event_info = {
                "Event name": event_name,
                "Venue": venue_name,
                "Tickets": tickets,
                "Start date": start_date,
                "End date": end_date,
                "Description": description
            }
            json_input = json.dumps(event_info)
            event_file.write(json_input)
            event_file.close()

def update_event():
    return



def delete_event(event_name: str) -> bool:
    # 1) Remove tickets from all users first
    refunded_count = Users.refund_event_tickets(event_name)
    print(f"Removed '{event_name}' tickets from {refunded_count} user(s).")

    # 2) Delete the event JSON file
    filename = event_name.replace(" ", "_").lower() + ".json"
    path = os.path.join("events", filename)

    if os.path.exists(path):
        os.remove(path)
        print("Event deleted.")
        return True
    else:
        print("Event file not found.")
        return False








def find_popular_events():
    print("\n=== Popular Upcoming Events===")

    if len(events) == 0:
        print("no event available")
        return

    popular_events = sorted(events, key=lambda event: event.tickets)

    for event in popular_events[:5]:
        print(event)

    # TO DO
    return


def filter_events_by_date():
    return


def filter_events_by_tickets_left():
    return


def filter_events_by_genre():
    return

def get_events_admin():
    return




def show_available_events():
    print("\n=== Available Events ===")
    print("1. Rock concert")
    print("2. Pop concert")
    print("3. International band performance")
    print("4. Local band performance")
    print("=========================\n")


def show_event_tickets(event_choice, filter_type=None, sort_type=None):
    events = {
        "1": {
            "name": "Rock concert",
            "date": "30-12-2025",
            "tickets": {
                "general": {"price": 25, "description": "General Admission"},
                "vip": {"price": 60, "description": "VIP Access + Lounge"},
                "meet_greet": {"price": 120, "description": "Meet & Greet Pass"}
            }
        },
        "2": {
            "name": "Pop concert",
            "date": "05-01-2026",
            "tickets": {
                "general": {"price": 35, "description": "General Admission"},
                "vip": {"price": 75, "description": "VIP Front Row"},
                "meet_greet": {"price": 150, "description": "Meet & Greet Pass"}
            }
        },
        "3": {
            "name": "International band performance",
            "date": "20-01-2026",
            "tickets": {
                "general": {"price": 30, "description": "General Admission"},
                "vip": {"price": 80, "description": "VIP Premium Seating"},
                "meet_greet": {"price": 200, "description": "Meet & Greet Backstage"}
            }
        },
        "4": {
            "name": "Local band performance",
            "date": "30-02-2026",
            "tickets": {
                "general": {"price": 20, "description": "General Admission"},
                "vip": {"price": 45, "description": "VIP Backstage Pass"},
                "meet_greet": {"price": 90, "description": "Meet & Greet Pass"}
            }
        }
    }

    if event_choice not in events:
        print("Invalid event choice!")
        return None, None

    event = events[event_choice]
    tickets = event["tickets"]

    if filter_type in ["vip", "general", "meet_greet"]:
        tickets = {filter_type: tickets[filter_type]}
    elif filter_type == "price_under_50":
        tickets = {k: v for k, v in tickets.items() if v["price"] < 50}
    elif filter_type == "price_over_50":
        tickets = {k: v for k, v in tickets.items() if v["price"] >= 50}

    if sort_type == "price_low_high":
        sorted_tickets = sorted(tickets.items(), key=lambda x: x[1]["price"])
    elif sort_type == "price_high_low":
        sorted_tickets = sorted(tickets.items(), key=lambda x: x[1]["price"], reverse=True)
    else:
        sorted_tickets = sorted(tickets.items())

    print(f"\n=== {event['name']} Ticket Options ===")
    option_map = {}
    count = 1
    for key, info in sorted_tickets:
        print(f"{count}. {key.title().replace('_', ' ')} - ${info['price']}")
        print(f"   {info['description']}")
        option_map[str(count)] = key
        count += 1
    print("===============================\n")
    return event, option_map





# def add_event(event_name, venue_id, start_date, end_date, description):
#     # TO DO
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         query = "INSERT INTO Events(event_name, venue_id, start_date, end_date, description) VALUES ('" + event_name +"', '" + str(venue_id) + "', '" + start_date + "', '" + end_date + "', '" + description + "');"
#         cursor.execute(enable_foreign_keys)
#         cursor.execute(query)
#         print("Event created")
#
#     except sqlite3.Error as error:
#         print("Error in Events.add_event(): " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.commit()
#             sqlite_connection.close()
#
# def get_all_events():
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         query = "SELECT * FROM EVENTS;"
#         cursor.execute(enable_foreign_keys)
#         cursor.execute(query)
#         result = cursor.fetchall()
#         if result:
#             return result
#         else:
#             return "No events exist please create one"
#
#
#     except sqlite3.Error as error:
#         print("Error in Events.get_all_events(): " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#
# def get_tickets_for_event(event_id):
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         # sqlite doesn't have foreign keys enabled by default must do this every connection
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         query = "SELECT * FROM Tickets WHERE event_id = " + str(event_id) + ";"
#         cursor.execute(enable_foreign_keys)
#         cursor.execute(query)
#         result = cursor.fetchall()
#         if result:
#             return result
#         else:
#             return "No tickets exist for this event please create some"
#
#
#     except sqlite3.Error as error:
#         print("Error: " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()

def get_all_events():
    # if there's no events
    if not os.path.isdir("events"):
        # TO CHANGE user cant make events
        return ["No events exist please create one"]
    else:
        event_list = []
        for file in os.listdir("events"):
            f = open("events/" + file, "r")
            file_info = json.loads(f.read())
            event_list.append(file_info)
            f.close()
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

from datetime import datetime

def _hardcoded_events():
    return [
        {"id": "1", "name": "Rock concert", "date": "30-12-2025", "genre": "Rock", "tickets_left": 50},
        {"id": "2", "name": "Pop concert", "date": "05-01-2026", "genre": "Pop", "tickets_left": 0},
        {"id": "3", "name": "International band performance", "date": "20-01-2026", "genre": "Rock", "tickets_left": 12},
        {"id": "4", "name": "Local band performance", "date": "30-02-2026", "genre": "Indie", "tickets_left": 7},
    ]

def filter_events_by_date_range(start_date_str, end_date_str):
    start = datetime.strptime(start_date_str, "%d-%m-%Y").date()
    end = datetime.strptime(end_date_str, "%d-%m-%Y").date()
    result = []
    for e in _hardcoded_events():
        d = datetime.strptime(e["date"], "%d-%m-%Y").date()
        if start <= d <= end:
            result.append(e)
    return result

def filter_events_by_tickets_left(min_left):
    min_left = int(min_left)
    return [e for e in _hardcoded_events() if int(e["tickets_left"]) >= min_left]

def filter_events_by_genre(genre):
    genre = genre.strip().lower()
    return [e for e in _hardcoded_events() if e["genre"].strip().lower() == genre]
