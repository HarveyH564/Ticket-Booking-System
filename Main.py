import datetime
import os
import json
from Events import Event
from Venue import Venue
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
            if file_info["Start date"] >= datetime.date.today() and file_info["Tickets"] != None:
                event_list.append(file_info["Event name"])
            f.close()
        # if there are events but none upcoming
        return event_list


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

def handle_input(user_input):
    if user_input == "<-":
        return

def create_account():
    invalid_username = True
    while invalid_username:
        username= input("Enter username: ")
        # previous menu
        if username == "<-":
            print()
            return False

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
                return False
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
            return True

# returns True if login was successful
def login():
    incorrect_username = True
    while incorrect_username:
        username = input("Enter username: ")
        # previous menu
        if username == "<-":
            print()
            return False

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
                    return False
                elif password_attempt == user_password:
                    user_file.close()
                    incorrect_password = True
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
        user_input = input("Select an option: Create an account [C], Login to an account [L]: ")
        if user_input == "C":
            attempt = create_account()
            if attempt == True:
                return True
        elif user_input == "L":
            attempt = login()
            if attempt == True:
                return True
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


def main():
    # TO DO

    logged_in = False
    while not logged_in:
        # will become true if user logs in or creates account
        logged_in = initial_menu()

    logged_in_menu()

    #admin = Admin()
    #admin.viewAllEvents(events)


if __name__ == "__main__":
    main()