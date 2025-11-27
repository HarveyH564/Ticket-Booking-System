import os
import json
import datetime

from Events import Event
from Admin import Admin

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

def findPopularEvents():
    print("\n=== Popular Upcoming Events===")

    if len(events) ==0:
        print("no event avaiable")
        return

    popular_events = sorted(events, key=lambda event: event.getTickets())
    
    for event in popular_events[:5]:
        print(event)

    # TO DO
    return
def filterEventsByDate():
    # TO DO
    return
def filterEventsByTicketsLeft():
    # TO DO
    return
def filterEventsByGenre():
    # TO DO
    return
def createUser():
    # TO DO
    return
def deleteUser():
    # TO DO
    return
def updateUser():
    # TO DO
    return
def createEventMap():
    # TO DO
    return
def createTicketMap():
    # TO DO
    return
def createTicket():
    # TO DO
    return
def deleteTicket():
    # TO DO
    return
def sendReminder():
    # TO DO
    return
def createQuestion():
    # TO DO
    return
def deleteQuestion():
    # TO DO
    return
def respondToQuestion():
    # TO DO
    return
def getEventsAdmin():
    # TO DO
    return
def updateEvent():
    # TO DO
    return
def deleteEvent():
    # TO DO
    return

def handleInput(userInput):
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

# start menu for initialising program
# returns true if login/create account was successful
def initial_menu():
    if not os.path.isdir("users"):
        os.mkdir("users")

    # Welcome msg
    print("Welcome to the project")
    print("Enter [<-] to go back to the previous menu")

    # Loops the menu unless user logs in or creates account
    while True:
        user_input = input("Select an option: Create an account [C], Login to an account [L]: ")
        if user_input == "C":
            attempt = create_account()
            if attempt[0] == True:
                return [True, attempt[1]]
        elif user_input == "L":
            attempt = login()
            if attempt[0] == True:
                return [True, attempt[1]]
        # previous menu
        elif user_input == "<-":
            print("Cannot go back from initial menu\n")

def logged_in_menu():
    user_input = input("Select an option: View all events [V], View upcoming available events [U] ")
    if user_input == "V":
        print(get_all_events())
    elif user_input == "U":
        print(get_available_events())
    return

def showAvailableEvents():
    # Available events
    print("\n=== Available Events ===")
    print("1. Rock concert")
    print("2. Pop concert")
    print("3. International band performance")
    print("4. Local band performance")
    print("=========================\n")


def showEventTickets(event_choice):
    # Display ticket options for selected event
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

    if event_choice in events:
        event = events[event_choice]
        print(f"\n=== {event['name']} Ticket Options ===")
        print(f"General Admission: ${event['general']}")
        print(f"VIP Ticket: ${event['vip']}")
        print("===============================")
        return event
    else:
        print("Invalid event choice!")
        return None


def purchaseTicket(username, event_choice, ticket_type, quantity):
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

    if event_choice in events:
        event = events[event_choice]

        if ticket_type == "1":  # General ticket
            ticket_name = f"{event['name']} - General Admission"
            price = event['general']
        elif ticket_type == "2":  # VIP ticket
            ticket_name = f"{event['name']} - VIP"
            price = event['vip']
        else:
            print("Invalid ticket type!")
            return False

        total_cost = price * quantity

        print(f"\nPurchase Summary:")
        print(f"Event: {event['name']}")
        print(f"Ticket Type: {ticket_name}")
        print(f"Quantity: {quantity}")
        print(f"Total: ${total_cost}")

        confirm = input("Confirm purchase? (Y/N): ").upper()

        if confirm == "Y":
            with open(f"users/{username}.json", "r") as file:
                userData = json.load(file)

            # Add ticket to user's tickets
            if ticket_name in userData["tickets"]:
                userData["tickets"][ticket_name] += quantity
            else:
                userData["tickets"][ticket_name] = quantity

            # Save updated user data
            with open(f"users/{username}.json", "w") as file:
                json.dump(userData, file)

            print("Purchase was successful, Thank you.")
            return True
        else:
            print("Purchase cancelled.")
            return False
    else:
        print("Invalid event choice!")
        return False


def userMenu(username):
    # Menu for logged-in users
    while True:
        print(f"\n=== Welcome to the Ticket System, {username}! ===")
        print("1. View Available Events")

        choice = input("Select an option (1): ")

        if choice == "1":
            showAvailableEvents()
            event_choice = input("Enter event number (1-4) or [<-] to go back: ")

            if event_choice == "<-":
                continue

            event = showEventTickets(event_choice)
            if event:
                print("Select ticket type:")
                print("1. General Admission")
                print("2. VIP")
                ticket_type = input("Enter ticket type (1-2): ")

                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity > 0:
                        purchaseTicket(username, event_choice, ticket_type, quantity)
                    else:
                        print("Quantity must be at least 1!")
                except ValueError:
                    print("Please enter a valid number!")
        elif choice == "<-":
            print("Use option 1 to view events")
        else:
            print("Invalid option! Please select 1 to view events.")


def Main():
    print("=== Simple Ticket System ===")

    logged_in = [False, False]
    while logged_in[0] == False:
        # will become true if user logs in or creates account
        logged_in = initial_menu()

    if logged_in[0]:
        logged_in_menu()
    #    userMenu(logged_in[1])

if __name__ == "__main__":
    Main()
