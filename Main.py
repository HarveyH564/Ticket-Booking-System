import os
import json

from Events import Event
from Admin import Admin

# testing with a events list can be change later
event1= Event()
event1.setVenue("Club21")
event1.setStartDate("12-12-2012")
event1.setEndDate("13-12-2012")
event1.setDescription("Studen night")
event1.setTickets(20)

events = [event1]




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
                    return True
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
            attempt = createAccount()
            if attempt == True:
                return True
        elif userInput == "L":
            attempt = login()
            if attempt == True:
                return True
        # previous menu
        elif userInput == "<-":
            print("Cannot go back from initial menu\n")


def Main():
    # TO DO

    loggedIn = False
    while not loggedIn:
        # will become true if user logs in or creates account
        loggedIn = initialMenu()

    admin = Admin()
    admin.viewAllEvents(events)

if __name__ == "__main__":
    Main()
    