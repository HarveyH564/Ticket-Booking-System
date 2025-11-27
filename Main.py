import os
import json

def getEvents():
    # TO DO
    return
def findPopularEvents():
    # TO DO
    return
def filterEventsByLocation():
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

def createAccount():
    invalidUsername = True
    while invalidUsername:
        username= input("Enter username: ")
        # previous menu
        if username == "<-":
            print()
            return False

        if os.path.exists("users/" + username + ".json"):
            print("Username is taken, please try again")
        else:
            userFile = open("users/" + username + ".json", "x")
            password = input("Enter password: ")
            # previous menu
            if password == "<-":
                userFile.close()
                os.remove("users/" + username + ".json")
                print()
                return False
            userInfo = {
                "username": username,
                "password": password,
                "tickets": {},
                "cart": {}
            }
            jsonInput = json.dumps(userInfo)
            userFile.write(jsonInput)
            userFile.close()
            invalidUsername = False
            print("Account creation successful")
            return username

# returns True if login was successful
def login():
    incorrectUsername = True
    while incorrectUsername:
        username = input("Enter username: ")
        # previous menu
        if username == "<-":
            print()
            return False

        # check user name
        if not os.path.exists("users/" + username + ".json"):
            print("User doesn't exist, please try again")
        else:
            incorrectUsername = False
            incorrectPassword = True
            userFile = open("users/" + username + ".json", "r")
            userInfo = json.loads(userFile.read())
            userPassword = userInfo["password"]

            # check password
            while incorrectPassword:
                passwordAttempt = input("Enter password: ")
                # previous menu
                if passwordAttempt == "<-":
                    userFile.close()
                    print()
                    incorrectPassword = True
                    return False
                elif passwordAttempt == userPassword:
                    userFile.close()
                    incorrectPassword = True
                    print("Login successful")
                    return username
                else:
                    print("Incorrect password, please try again")

# start menu for initialising program
# returns true if login/create account was successful
def initialMenu():
    # Welcome msg
    print("Welcome to the project")
    print("Enter [<-] to go back to the previous menu")

    # Loops the menu unless user logs in or creates account
    while True:
        userInput = input("Select an option: Create an account [C], Login to an account [L]: ")
        if userInput == "C":
            username = createAccount()  # Made change here to get username
            if username:
                return username
        elif userInput == "L":
            username = login()
            if username:
                return username # Before was return true
        elif userInput == "<-":
            print("Cannot go back from initial menu\n")


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
    # Create users directory if it doesn't exist
    if not os.path.exists("users"):
        os.makedirs("users")

    print("=== Simple Ticket System ===")

    while True:
        username = initialMenu()

        if username:
            userMenu(username)

        # Ask if user wants to exit completely
        exit_choice = input("Do you want to exit the program? (Y/N): ").upper()
        if exit_choice == "Y":
            print("Thank you for using the Ticket System!")
            break


if __name__ == "__main__":
    Main()