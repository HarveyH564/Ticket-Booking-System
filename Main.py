import os
import json
from Events import Event
from Admin import Admin


def get_events():
    # TO DO
    return
def find_popular_events():
    # TO DO
    return
def filter_events_by_location():
    # TO DO
    return
def filter_events_by_date():
    # TO DO
    return
def filter_events_by_tickets_left():
    # TO DO
    return
def filter_events_by_genre():
    # TO DO
    return
def create_user():
    # TO DO
    return
def delete_user():
    # TO DO
    return
def update_user():
    # TO DO
    return
def create_event_map():
    # TO DO
    return
def create_ticket_map():
    # TO DO
    return
def create_ticket():
    # TO DO
    return
def delete_ticket():
    # TO DO
    return
def send_reminder():
    # TO DO
    return
def create_question():
    # TO DO
    return
def delete_question():
    # TO DO
    return
def respond_to_question():
    # TO DO
    return
def get_events_admin():
    # TO DO
    return
def update_event():
    # TO DO
    return
def delete_event():
    # TO DO
    return

def handle_input(userInput):
    if userInput == "<-":
        return

def create_account():
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
            return True

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
        if not os.path.exists("users/" + username + ".json") or not os.isdir():
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
                    return True
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
        userInput = input("Select an option: Create an account [C], Login to an account [L]: ")
        if userInput == "C" or "c":
            attempt = create_account()
            if attempt == True:
                return True
        elif userInput == "L" or "l":
            attempt = login()
            if attempt == True:
                return True
        # previous menu
        elif userInput == "<-":
            print("Cannot go back from initial menu\n")


def Main():
    # TO DO

    # testing with a events list can be change later
    #event1 = Event()
    #event1.setVenue("Club21")
    #event1.setStartDate("12-12-2012")
    #event1.setEndDate("13-12-2012")
    #event1.setDescription("Student night")
    #event1.setTickets(20)

    #events = [event1]

    loggedIn = False
    while not loggedIn:
        # will become true if user logs in or creates account
        loggedIn = initial_menu()

    #admin = Admin()
    #admin.viewAllEvents(events)


Main()