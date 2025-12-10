import Users
import Events
import Tickets

def handle_input(userInput):
    if userInput == "<-":
        return

def initial_menu():
    print("Welcome to the project")
    print("Enter [<-] to go back to the previous menu")

    while True:
        user_input = input("Select an option: Create an account [C], Login to an account [L]: ")
        if user_input == "C":
            attempt = Users.create_account()
            if attempt[0] is True:
                return [True, attempt[1]]
        elif user_input == "L":
            attempt = Users.login()
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

def view_all_events_menu(event_list, username):
    print("\n")
    event_index = 0
    for event in event_list:
        print(str(event_index + 1) + ". Event name: " + event[1])
        print("\tStart date: " + event[3])
        print("\tDescription: " + event[5] + "\n")
        event_index += 1

    at_events_menu = True
    while at_events_menu:
        user_input = input("Select an event or go back [1, 2, ..., <-]: ")
        try:
            if user_input == "<-":
                at_events_menu = True
                user_menu(username)
            elif int(user_input) <= event_index:
                # get event
                event = event_list[int(user_input) - 1]
                print(event[1])
            else:
                print("No event of index", user_input)
        except:
            print("Invalid input")



def user_menu(username):
    # Menu for logged-in users
    at_user_menu = True
    while at_user_menu:
        print(f"\n=== Welcome to the Ticket System, {username}! ===")
        print("1. View Available Events")
        print("2. Update User Details")  # <-- Added option
        print("3. View All Events")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            Events.show_available_events()
            event_choice = input("Enter event number (1-4) or [<-] to go back: ")

            if event_choice == "<-":
                continue

            current_filter = None
            current_sort = None

            event, ticket_options = Events.show_event_tickets(event_choice, current_filter, current_sort)

            if event:
                print("1. Buy Ticket")
                print("2. Filter / Sort Tickets")
                action = input("Select: ")

                if action == "2":
                    event, ticket_options, current_filter, current_sort = Tickets.apply_filters_and_sorting(
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
                        Tickets.purchase_ticket(username, event_choice, ticket_type, quantity)
                    else:
                        print("Quantity must be at least 1!")
                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "2":  # update details
            Users.update_user_details(username)
            username = username  # session username already updated inside function

        elif choice == "3":
            all_events = Events.get_all_events()
            if all_events == "No events exist please create one":
                print("No events\n")
            else:
                at_user_menu = False
                view_all_events_menu(all_events, username)

        elif choice == "<-":
            print("Cannot go back from main menu")
        else:
            print("Invalid option! Please select 1 or 2.")