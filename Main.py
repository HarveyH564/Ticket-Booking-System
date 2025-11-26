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
        # if user wants to go back
        if username == "<-":
            print()
            return initialMenu()

        if os.path.exists("users/" + username + ".json"):
            print("Username is taken, please try again")
        else:
            userFile = open("users/" + username + ".json", "x")
            password = input("Enter password: ")
            # if user wants to go back
            if password == "<-":
                userFile.close()
                os.remove("users/" + username + ".json")
                print()
                return initialMenu()
            userInfo = {
                "Username": username,
                "Password": password,
                "Tickets": {},
                "Cart": {}
            }
            jsonInput = json.dumps(userInfo)
            userFile.write(jsonInput)
            userFile.close()
            invalidUsername = False

def login():
    print("Enter username:")
    username = input()
    if not os.path.exists("users/" + username + ".json"):
        print("User doesn't exist, please try again")


def initialMenu():
    # Welcome msg
    print("Welcome to the project")
    print("Enter [<-] to go back to the previous menu")

    # Decides whether to navigate to create account or login
    choicePending = True
    while choicePending:
        print("Select an option: Create an account [C], Login to an account [L]")
        userInput = input()
        if userInput == "C":
            createAccount()
            choicePending = True
        elif userInput == "L":
            login()
            choicePending = True
        elif userInput == "<-":
            print("Cannot go back from initial menu\n")


def Main():
    # TO DO
    initialMenu()


start = Main()