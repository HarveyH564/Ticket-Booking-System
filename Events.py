import json
import os
import Users
import datetime
import sqlite3


EVENTS = {
    "1": {"name": "Rock concert", "date": "30-05-2026", "genre": "Rock", "tickets_left": 50,
          "prices": {"general": 25, "vip": 60, "meet_greet": 120}},
    "2": {"name": "Pop concert", "date": "05-09-2026", "genre": "Pop", "tickets_left":80,
          "prices": {"general": 35, "vip": 75, "meet_greet": 150}},
    "3": {"name": "International band performance", "date": "20-01-2026", "genre": "Rock", "tickets_left": 12,
          "prices": {"general": 30, "vip": 80, "meet_greet": 200}},
    "4": {"name": "Local band performance", "date": "30-02-2026", "genre": "Indie", "tickets_left": 17,
          "prices": {"general": 20, "vip": 45, "meet_greet": 90}},
}


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






def show_event_tickets(event_choice, filter_type=None, sort_type=None):
    if event_choice not in EVENTS:
        print("Invalid event choice!")
        return None, None

    event = EVENTS[event_choice]
    tickets = event["prices"]

    ticket_meta = {
        "general": {"price": tickets["general"], "description": "General Admission"},
        "vip": {"price": tickets["vip"], "description": "VIP Access"},
        "meet_greet": {"price": tickets["meet_greet"], "description": "Meet & Greet"}
    }

    if filter_type in ["vip", "general", "meet_greet"]:
        ticket_meta = {filter_type: ticket_meta[filter_type]}
    elif filter_type == "price_under_50":
        ticket_meta = {k: v for k, v in ticket_meta.items() if v["price"] < 50}
    elif filter_type == "price_over_50":
        ticket_meta = {k: v for k, v in ticket_meta.items() if v["price"] >= 50}

    if sort_type == "price_low_high":
        sorted_tickets = sorted(ticket_meta.items(), key=lambda x: x[1]["price"])
    elif sort_type == "price_high_low":
        sorted_tickets = sorted(ticket_meta.items(), key=lambda x: x[1]["price"], reverse=True)
    else:
        sorted_tickets = sorted(ticket_meta.items())

    print(f"\n=== {event['name']} Ticket Options ===")
    print(f"Tickets left: {event['tickets_left']}")
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
    if not os.path.isdir("events"):
        return ["No events exist please create one"]
    else:
        event_list = []
        for file in os.listdir("events"):
            f = open("events/" + file, "r")
            file_info = json.loads(f.read())

            event_tuple = (
                file_info.get("Event name", ""),      # Index 0
                file_info.get("Event name", ""),      # Index 1 (same as 0 for now)
                file_info.get("Venue", ""),           # Index 2
                file_info.get("Start date", ""),      # Index 3
                file_info.get("End date", ""),        # Index 4
                file_info.get("Description", "")      # Index 5
            )
            event_list.append(event_tuple)
            f.close()
        return event_list

def get_available_event_ids():
    return [eid for eid, e in EVENTS.items() if e.get("tickets_left", 0) > 0]


def show_available_events():
    print("\n=== Available Events ===")
    available = get_available_event_ids()

    if not available:
        print("No available events (all sold out).")
        print("=========================\n")
        return

    for eid in available:
        e = EVENTS[eid]
        print(f"{eid}. {e['name']} ({e['date']}) - {e['tickets_left']} left")
    print("=========================\n")

from datetime import datetime

def filter_events_by_date_range(start_date_str, end_date_str):
    start = datetime.strptime(start_date_str, "%d-%m-%Y").date()
    end = datetime.strptime(end_date_str, "%d-%m-%Y").date()

    results = []
    for eid, e in EVENTS.items():
        try:
            d = datetime.strptime(e["date"], "%d-%m-%Y").date()
        except ValueError:
            # skips invalid dates like 30-02-2026
            continue

        if start <= d <= end:
            results.append({"id": eid, **e})
    return results


def filter_events_by_tickets_left(min_left):
    min_left = int(min_left)

    results = []
    for eid, e in EVENTS.items():
        if int(e.get("tickets_left", 0)) >= min_left:
            results.append({"id": eid, **e})
    return results


def filter_events_by_genre(genre):
    genre = genre.strip().lower()

    results = []
    for eid, e in EVENTS.items():
        if e.get("genre", "").strip().lower() == genre:
            results.append({"id": eid, **e})
    return results