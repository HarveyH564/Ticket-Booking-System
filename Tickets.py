import os
import json
import time
import random
import Events
from datetime import datetime


class Ticket():
    def __init__(self):
        # TO DO
        self.id = None
        self.purchased = False
        self.user_id = None
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

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type


def create_ticket_map():
    return


def create_ticket():
    return


def delete_ticket():
    return


def send_reminder():
    return


# what is this function for????
def apply_filters_and_sorting(event_choice, current_filter=None, current_sort=None):
    filter_type = current_filter
    sort_type = current_sort

    while True:
        print("\n=== Filter & Sort Options ===")
        print("1. Apply Filter")
        print("2. Apply Sorting")
        print("3. View Tickets With Current Settings")
        print("4. Clear Filters/Sorting")
        print("5. Back")

        ch = input("Select option: ")

        if ch == "1":
            print("\nFilters:")
            print("1. VIP Only")
            print("2. General Only")
            print("3. Meet & Greet Only")
            print("4. Price Under $50")
            print("5. Price $50 And Above")
            print("6. Remove Filter")

            f = input("Select: ")
            filter_map = {
                "1": "vip",
                "2": "general",
                "3": "meet_greet",
                "4": "price_under_50",
                "5": "price_over_50",
                "6": None
            }
            filter_type = filter_map.get(f, filter_type)

        elif ch == "2":
            print("\nSort:")
            print("1. Price Low → High")
            print("2. Price High → Low")
            print("3. Alphabetical")
            print("4. Remove Sorting")

            s = input("Select: ")
            sort_map = {
                "1": "price_low_high",
                "2": "price_high_low",
                "3": None,
                "4": None
            }
            sort_type = sort_map.get(s, sort_type)

        elif ch == "3":
            event, ticket_options = Events.show_event_tickets(event_choice, filter_type, sort_type)
            return event, ticket_options, filter_type, sort_type

        elif ch == "4":
            filter_type = None
            sort_type = None
            print("Filters cleared.")

        elif ch == "5":
            return None, None, filter_type, sort_type


def purchase_ticket(username, event_choice, ticket_type, quantity):
    events = Events.EVENTS

    if event_choice not in events:
        print("Invalid event choice!")
        return False

    event = events[event_choice]

    tickets_left = int(event.get("tickets_left", 0))
    if tickets_left <= 0:
        print("Sorry, this event is sold out!")
        return False

    if quantity <= 0:
        print("Quantity must be at least 1.")
        return False

    if quantity > tickets_left:
        print(f"Only {tickets_left} tickets left.")
        return False

    ticket_map = {"1": "general", "2": "vip", "3": "meet_greet"}
    if ticket_type not in ticket_map:
        print("Invalid ticket type!")
        return False

    ticket_key = ticket_map[ticket_type]

    prices = event.get("prices", {})
    if ticket_key not in prices:
        print("Ticket type not available for this event.")
        return False

    price = prices[ticket_key]
    ticket_name = f"{event['name']} - {ticket_key.replace('_', ' ').title()}"
    total_cost = price * quantity
    reference = f"REF-{username}-{int(time.time())}-{random.randint(1000, 9999)}"

    print("\n" + "=" * 50)
    print("BOOKING SUMMARY")
    print("=" * 50)
    print(f"Event: {event['name']}")
    print(f"Date: {event['date']}")
    print(f"Ticket Type: {ticket_key.replace('_', ' ').title()}")
    print(f"Quantity: {quantity}")
    print(f"Price per ticket: ${price}")
    print(f"Total Cost: ${total_cost}")
    print(f"Booking Reference: {reference}")
    print("=" * 50 + "\n")

    confirm = input("Confirm purchase? (Y/N): ").upper()

    if confirm == "Y":
        # reduce tickets (OPTION 1: only lasts while program is running)
        event["tickets_left"] = tickets_left - quantity

        os.makedirs("users", exist_ok=True)
        path = f"users/{username}.json"

        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump({"ticket_records": []}, f)

        with open(path, "r") as file:
            userData = json.load(file)

        userData.setdefault("ticket_records", []).append({
            "reference": reference,
            "ticket": ticket_name,
            "quantity": quantity,
            "event_date": event["date"],
            "purchase_date": datetime.now().strftime("%d-%m-%Y"),
            "total_paid": total_cost
        })

        with open(path, "w") as file:
            json.dump(userData, file, indent=2)

        print("\nPurchase successful!")
        print(f"Your unique booking reference is: {reference}\n")

        if event["tickets_left"] == 0:
            print("This event is now SOLD OUT.")

        print("1. Download Ticket")
        print("2. Back to menu")
        post = input("Select: ")
        if post == "1":
            print("Ticket successfully downloaded!")

        return True
    else:
        print("Purchase cancelled.")
        return False

def view_previous_purchases(username):
    path = f"users/{username}.json"

    if not os.path.exists(path):
        print("No previous purchases found")
        return

    with open(path, "r") as file:
        userData = json.load(file)

    records = userData.get("ticket_records", [])

    if not records:
        print("No previous purchases found")
        return

    print("\n" + "=" * 60)
    print("PURCHASE HISTORY")
    print("=" * 60)

    for i, r in enumerate(records, start=1):
        print(f"\n{i}. {r.get('ticket', 'Unknown event')}")
        print(f"   Reference: {r.get('reference', 'N/A')}")
        print(f"   Quantity: {r.get('quantity', 'N/A')}")
        if r.get('event_date'):
            print(f"   Event Date: {r['event_date']}")
        if r.get('total_paid'):
            print(f"   Total Paid: ${r['total_paid']}")
        print("   " + "-" * 40)

    print("=" * 60)


def add_ticket_to_cart(ticket, user):
    if not os.path.exists("users/" + user + ".json"):
        print("User doesn't exist, please try again")
    else:
        file = open("users/" + user + ".json", "r")
        user_info = json.loads(file.read())
        if user_info["cart"] == None:
            user_info["cart"][ticket] = 1
        else:
            user_info["cart"][ticket] = 1
        file = open("users/" + user + ".json", "w")
        json.dump(user_info, file)
        file.close()


def remove_ticket_from_cart(ticket, user):
    if not os.path.exists("users/" + user + ".json"):
        print("User doesn't exist, please try again")
    else:
        file = open("users/" + user + ".json", "r+")
        user_info = json.loads(file.read())
        if user_info["cart"] is None:
            print("User has no tickets")
        else:
            if ticket in user_info["cart"]:
                user_info["cart"].pop(ticket)
                file = open("users/" + user + ".json", "w")
                json.dump(user_info, file)
                print("Ticket removed!")
            else:
                print("Ticket already removed!")
        file.close()