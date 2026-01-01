import Users
import Events
import Tickets
import json
from datetime import datetime, timedelta


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


def show_seat_map():
    print("\n=== Seat Map (O = available, X = occupied) ===")
    print("    1  2  3  4  5")
    print("A | O  O  X  O  O")
    print("B | O  X  O  O  O")
    print("C | O  O  O  X  O")
    print("D | O  O  O  O  O")
    print("E | O  O  O  O  X")
    print("============================================\n")


def view_all_events_menu(event_list, user_id):
    print("\n")
    event_index = 0
    for event in event_list:
        print(str(event_index + 1) + ". Event name: " + event[1])
        print("\tStart date: " + event[3])
        print("\tDescription: " + event[5] + "\n")
        event_index += 1

    while True:
        user_input = input("Select an event or go back [1, 2, ..., <-]: ")
        try:
            if user_input == "<-":
                return  # Fixed: Simply return, don't call user_menu
            elif int(user_input) <= event_index:
                # get event
                event = event_list[int(user_input) - 1]
                print(event[1])
            else:
                print("No event of index", user_input)
        except:
            print("Invalid input")


# Admin functions
def admin_login():
    """Simple admin login"""
    print("\n=== ADMIN LOGIN ===")
    username = input("Admin Username: ")
    password = input("Password: ")

    if username == "Admin" and password == "1234":
        print("Admin login successful!")
        return True
    else:
        print("Invalid admin credentials!")
        return False
def admin_manage_user_menu():
    while True:
        print("\n=== ADMIN MANAGE USER ===")
        print("1. View all user")
        print("2. add new users")
        print("3. update user")
        print("4. delete user")
        print("5. Back")

        choice=input("Select an option (1-5): ")

        if choice == "1":
            users = Users.list_all_users()

            if not users:
                print("No users found!")

            else:
                print("\n User:")
                for u in users:
                    print(f" - {u}")

        elif choice == "2":
            username = input("New Username: ").strip()
            password = input("New Password: ").strip()

            if Users.create_user(username, password):
                print("User created successfully!")

            else:
                print("username already taken!")
        elif choice == "3":
            old_username = input("Current Username: ").strip()

            if not Users.user_exists(old_username):
                print("User does not exist!")
                continue

            user = Users.load_user(old_username)

            print("Leave blank to keep current username/password.")
            new_username = input("New Username: ").strip()
            new_password = input("New Password: ").strip()

            if not new_username:
                new_username = old_username

            current_password = user.get("password,")
            if not new_password != new_password:
                new_password = user["password"]

            success = Users.update_user(old_username, new_username, new_password)

            if success:
                print("User successfully updated!")
            else:
                print("Update failed (maybe new username already taken).")



        elif choice == "4":
            username = input("Username to delete: ").strip()
            if Users.delete_user(username):
                print("User deleted.")
            else:
                print("User not found.")


        elif choice == "5" or choice == "<-":
            return

        else:
            print("Invalid option.")


def admin_menu():
    """Admin menu for managing questions"""
    import Questions

    while True:
        print("\n=== ADMIN PANEL ===")
        print("1. View & Reply to User Questions")
        print("2. View all events")
        print("3. Manage user accounts (add/update/delete user account")
        print("4. Logout")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            # Get unanswered questions
            questions = Questions.get_unanswered_questions()

            if not questions:
                print("\nNo new questions from users.")
                continue

            print(f"\n=== User Questions ({len(questions)} unanswered) ===")
            for q in questions:
                print(f"\nQuestion ID: {q['id']}")
                print(f"From: {q['user']}")
                print(f"Question: {q['question']}")
                print(f"Time: {q['timestamp']}")

                response = input("\nType response (or press Enter to skip, 'delete' to remove): ")

                if response.strip().lower() == "delete":
                    if Questions.delete_question(q['id']):
                        print("Question deleted!")
                    else:
                        print("Failed to delete question.")
                elif response.strip():
                    if Questions.respond_to_question(q['id'], response):
                        print("Response sent!")
                    else:
                        print("Failed to send response.")
                else:
                    print("Skipped this question.")

        elif choice == "2":
            Events.show_available_events()


        elif choice == "3":
            admin_manage_user_menu()


        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option! Please select 1-3.")



def user_menu(user_id):
    # Menu for logged-in users
    # user_id is actually the username (from JSON system)
    username = user_id

    # Check for reminders
    try:
        today = datetime.now().date()
        with open(f"users/{username}.json", "r") as f:
            user_data = json.load(f)

        reminders = []
        if "ticket_records" in user_data:
            for record in user_data["ticket_records"]:
                if "event_date" in record:
                    try:
                        event_date = datetime.strptime(record["event_date"], "%d-%m-%Y").date()
                        days_left = (event_date - today).days
                        if 0 <= days_left <= 7:
                            # Get event name from ticket or extract from ticket name
                            ticket_name = record.get("ticket", "")
                            event_name = ticket_name.split(" - ")[0] if " - " in ticket_name else "Event"
                            reminders.append((event_name, record["event_date"], days_left))
                    except ValueError as e:
                        print(f"Debug: Could not parse date {record['event_date']}: {e}")

        if reminders:
            print("\n" + "=" * 50)
            print("UPCOMING EVENT REMINDERS:")
            print("=" * 50)
            for event_name, event_date, days_left in reminders:
                if days_left == 0:
                    print(f"• {event_name} - TODAY! ({event_date})")
                elif days_left == 1:
                    print(f"• {event_name} - TOMORROW! ({event_date})")
                else:
                    print(f"• {event_name} - in {days_left} days ({event_date})")
            print("=" * 50)
        else:
            print("\n No upcoming events in the next 7 days.\n")
    except Exception as e:
        print(f"Note: Could not check reminders: {e}")

    at_user_menu = True
    while at_user_menu:
        print(f"\n=== Welcome to the Ticket System, {username}! ===")
        print("1. View Available Events")
        print("2. View Popular Upcoming Events")
        print("3. View All Events")
        print("4. Update User Details")
        print("5. View previous purchases")
        print("6. Logout")

        choice = input("Select an option (1-6): ")

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
                print("3. View Seating Map")
                action = input("Select: ")

                if action == "3":
                    show_seat_map()
                elif action == "<-":
                    break

                if action == "2":
                    event, ticket_options, current_filter, current_sort = Tickets.apply_filters_and_sorting(
                        event_choice, current_filter, current_sort
                    )
                    # Back button
                    if event is None or ticket_options is None:
                        continue

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


        elif choice == "2":
            print('\n=== Popular Upcoming Events====')
            print("1.Rock concert")
            print("2.Christmas Party")


        elif choice == "3":
            all_events = Events.get_all_events()
            if all_events == "No events exist please create one":
                print("No events\n")
            else:
                view_all_events_menu(all_events, user_id)


        elif choice == "4":
            Users.update_user_details(username)


        elif choice == "5":
            Tickets.view_previous_purchases(username)

        elif choice == "6":
            print("Logging out...")
            at_user_menu = False

        elif choice == "<-":
            print("Cannot go back from main menu")
        else:
            print("Invalid option! Please select 1-6.")