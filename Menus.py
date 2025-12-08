import os
import User
import Events

def initial_menu():
    if not os.path.isdir("users"):
        os.mkdir("users")

    print("Welcome to the project")
    print("Enter [<-] to go back to the previous menu")

    while True:
        user_input = input("Select an option: Create an account [C], Login to an account [L]: ")
        if user_input == "C":
            attempt = User.create_account()
            if attempt[0] is True:
                return [True, attempt[1]]
        elif user_input == "L":
            attempt = User.login()
            if attempt[0] is True:
                return [True, attempt[1]]
        elif user_input == "<-":
            print("Cannot go back from initial menu\n")

def logged_in_menu():
    user_input = input("Select an option: View all events [V], View upcoming available events [U] ")
    if user_input == "V":
        print(Events.get_all_events())
    elif user_input == "U":
        print(Events.get_available_events())
    return