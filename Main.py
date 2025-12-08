import os
import json
import time
import random
import Menus
from Events import Event


# testing with a events list can be changed later
event1 = Event()
# Using direct attributes instead of setters to avoid AttributeError
event1.venue = "Club21"
event1.start_date = "12-12-2012"
event1.end_date = "13-12-2012"
event1.description = "Student night"
event1.tickets = 20

events = [event1]

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


def create_user():
    return


def delete_user():
    return


def update_user():
    return


def create_event_map():
    return


def create_ticket_map():
    return


def create_ticket():
    return


def delete_ticket():
    return


def send_reminder():
    return


def create_question():
    return


def delete_question():
    return


def respond_to_question():
    return


def get_events_admin():
    return


def update_event():
    return


def delete_event():
    return


def handle_input(userInput):
    if userInput == "<-":
        return

def create_account():
    invalid_username = True
    while invalid_username:
        username= input("Enter username: ")
        # previous menu
        if username == "<-":
            print()
            return [False, False]

        if os.path.exists("users/" + username + ".json"):
            print("Username is taken, please try again")
        else:
            user_file = open("users/" + username + ".json", "x")
            password = input("Enter password: ")
            # previous menu
            if password == "<-":
                user_file.close()
                os.remove("users/" + username + ".json")
                print()
                return [False, False]
            user_info = {
                "username": username,
                "password": password,
                "tickets": {},
                "cart": {}
            }
            json_input = json.dumps(user_info)
            user_file.write(json_input)
            user_file.close()
            invalid_username = False
            print("Account creation successful")
            return [True, username]

# returns True if login was successful
def login():
    incorrect_username = True
    while incorrect_username:
        username = input("Enter username: ")
        # previous menu
        if username == "<-":
            print()
            return [False, False]

        # check user name
        if not os.path.exists("users/" + username + ".json"):
            print("User doesn't exist, please try again")
        else:
            incorrect_username = False
            incorrect_password = True
            user_file = open("users/" + username + ".json", "r")
            user_info = json.loads(user_file.read())
            user_password = user_info["password"]

            # check password
            while incorrect_password:
                password_attempt = input("Enter password: ")
                # previous menu
                if password_attempt == "<-":
                    user_file.close()
                    print()
                    incorrect_password = True
                    return [False, False]
                elif password_attempt == user_password:
                    user_file.close()
                    incorrect_password = True
                    print("Login successful")
                    return [True, username]
                else:
                    print("Incorrect password, please try again")

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
            "tickets": {
                "general": {"price": 25, "description": "General Admission"},
                "vip": {"price": 60, "description": "VIP Access + Lounge"},
                "meet_greet": {"price": 120, "description": "Meet & Greet Pass"}
            }
        },
        "2": {
            "name": "Pop concert",
            "tickets": {
                "general": {"price": 35, "description": "General Admission"},
                "vip": {"price": 75, "description": "VIP Front Row"},
                "meet_greet": {"price": 150, "description": "Meet & Greet Pass"}
            }
        },
        "3": {
            "name": "International band performance",
            "tickets": {
                "general": {"price": 30, "description": "General Admission"},
                "vip": {"price": 80, "description": "VIP Premium Seating"},
                "meet_greet": {"price": 200, "description": "Meet & Greet Backstage"}
            }
        },
        "4": {
            "name": "Local band performance",
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
            event, ticket_options = show_event_tickets(event_choice, filter_type, sort_type)
            return event, ticket_options, filter_type, sort_type

        elif ch == "4":
            filter_type = None
            sort_type = None
            print("Filters cleared.")

        elif ch == "5":
            return None, None, filter_type, sort_type


def purchase_ticket(username, event_choice, ticket_type, quantity):
    events = {
        "1": {
            "name": "Rock concert",
            "general": 25,
            "vip": 60
        },
        "2": {
            "name": "Pop concert",
            "general": 35,
            "vip": 75
        },
        "3": {
            "name": "International band performance",
            "general": 30,
            "vip": 80
        },
        "4": {
            "name": "Local band performance",
            "general": 20,
            "vip": 45
        }
    }

    if event_choice not in events:
        print("Invalid event choice!")
        return False

    event = events[event_choice]
    ticket_map = {"1": "general", "2": "vip", "3": "meet_greet"}

    if ticket_type not in ticket_map:
        print("Invalid ticket type!")
        return False

    ticket_key = ticket_map[ticket_type]
    ticket_name = f"{event['name']} - {ticket_key.replace('_', ' ').title()}"
    price = event[ticket_key]
    total_cost = price * quantity
    reference = f"REF-{username}-{int(time.time())}-{random.randint(1000, 9999)}"

    print(f"\nPurchase Summary:")
    print(f"Event: {event['name']}")
    print(f"Ticket Type: {ticket_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total_cost}")
    print(f"Booking Reference: {reference}")

    confirm = input("Confirm purchase? (Y/N): ").upper()

    if confirm == "Y":
        with open(f"users/{username}.json", "r") as file:
            userData = json.load(file)

        if "ticket_records" not in userData:
            userData["ticket_records"] = []

        userData["ticket_records"].append(
            {"reference": reference, "ticket": ticket_name, "quantity": quantity}
        )

        with open(f"users/{username}.json", "w") as file:
            json.dump(userData, file)

        print("\nPurchase successful!")
        print(f"Your unique booking reference is: {reference}\n")
        return True
    else:
        print("Purchase cancelled.")
        return False


# Update details section
def update_user_details(username):
    user_file_path = f"users/{username}.json"
    if not os.path.exists(user_file_path):
        print("User file not found!")
        return

    with open(user_file_path, "r") as file:
        user_data = json.load(file)

    print("\n=== Update User Details ===")
    new_username = input(f"Enter new username (leave blank to keep '{user_data['username']}'): ")
    new_password = input("Enter new password (leave blank to keep current password): ")

    if new_username:
        new_user_file_path = f"users/{new_username}.json"
        if os.path.exists(new_user_file_path):
            print("Username already taken, please try again.")
            return
        os.rename(user_file_path, new_user_file_path)
        user_data["username"] = new_username
        username = new_username

    if new_password:
        user_data["password"] = new_password

    with open(f"users/{username}.json", "w") as file:
        json.dump(user_data, file)

    print("User details updated successfully!\n")


def user_menu(username):
def userMenu(username):
    # Menu for logged-in users
    while True:
        print(f"\n=== Welcome to the Ticket System, {username}! ===")
        print("1. View Available Events")
        print("2. Update User Details")  # <-- Added option

        choice = input("Select an option (1-2): ")

        if choice == "1":
            show_available_events()
            event_choice = input("Enter event number (1-4) or [<-] to go back: ")

            if event_choice == "<-":
                continue

            current_filter = None
            current_sort = None

            event, ticket_options = show_event_tickets(event_choice, current_filter, current_sort)

            if event:
                print("1. Buy Ticket")
                print("2. Filter / Sort Tickets")
                action = input("Select: ")

                if action == "2":
                    event, ticket_options, current_filter, current_sort = apply_filters_and_sorting(
                        event_choice, current_filter, current_sort
                    )

                print("Select ticket number to buy:")
                ticket_num = input("Enter: ")

                if ticket_num not in ticket_options:
                    print("Invalid selection.")
                    continue

                type_map = {"general": "1", "vip": "2", "meet_greet": "3"}
                ticket_key = ticket_options[ticket_num]
                ticket_type = type_map[ticket_key]

                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity > 0:
                        purchase_ticket(username, event_choice, ticket_type, quantity)
                    else:
                        print("Quantity must be at least 1!")
                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "2":  # update details
            update_user_details(username)
            username = username  # session username already updated inside function

        elif choice == "<-":
            print("Use option 1 to view events")
        else:
            print("Invalid option! Please select 1 or 2.")


def logged_in_menu():
    user_input = input("Select an option: View all events [V], View upcoming available events [U] ")
    if user_input == "V":
        print(get_all_events())
    elif user_input == "U":
        print(get_available_events())
    return
        elif choice == "<-":
            print("Use option 1 to view events")
        else:
            print("Invalid option! Please select 1 to view events.")

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




def main():
    print("=== Simple Ticket System ===")
    logged_in = [False, False]
    while not logged_in[0]:
        logged_in = Menus.initial_menu()

    if logged_in[0]:
        user_menu(logged_in[1])
    logged_in_menu()
       Menus.user_menu(logged_in[1])
    Menus.logged_in_menu()


if __name__ == "__main__":
    main()
