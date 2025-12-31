import Users
import Events
import Tickets
import json
import os
from datetime import datetime, timedelta


def handle_input(userInput):
    if userInput == "<-":
        return


def initial_menu():
    if not os.path.isdir("users"):
        os.mkdir("users")


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
        else:
            print("Invalid option! Please select C or L.")


# def logged_in_menu():
#     user_input = input("Select an option: View all events [V], View upcoming available events [U] ")
#     if user_input == "V":
#         print(Events.get_all_events())
#     elif user_input == "U":
#         print(Events.get_available_events())
#     return

def user_menu(username):
#     # Menu for logged in users
#
#     sqlite_connection = None
#     try:
#         import sqlite3
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         query = "SELECT username FROM Users WHERE user_id = " + str(user_id) + ";"
#         cursor.execute(query)
#         result = cursor.fetchone()
#         if result:
#             username = result[0]  # Now we have the username
#         else:
#             print("Error: Could not find username for user ID", user_id)
#             return
#     except Exception as error:
#         print("Error getting username: " + str(error))
#         return
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()

    # # Check for reminders
    # try:
    #     today = datetime.now().date()
    #     with open(f"users/{username}.json", "r") as f:
    #         user_data = json.load(f)
    #
    #     reminders = []
    #     if "ticket_records" in user_data:
    #         for record in user_data["ticket_records"]:
    #             if "event_date" in record:
    #                 try:
    #                     event_date = datetime.strptime(record["event_date"], "%d-%m-%Y").date()
    #                     days_left = (event_date - today).days
    #                     if 0 <= days_left <= 7:
    #                         # Get event name from ticket or extract from ticket name
    #                         ticket_name = record.get("ticket", "")
    #                         event_name = ticket_name.split(" - ")[0] if " - " in ticket_name else "Event"
    #                         reminders.append((event_name, record["event_date"], days_left))
    #                 except ValueError as e:
    #                     print(f"Debug: Could not parse date {record['event_date']}: {e}")
    #
    #     if reminders:
    #         print("\n" + "=" * 50)
    #         print("UPCOMING EVENT REMINDERS:")
    #         print("=" * 50)
    #         for event_name, event_date, days_left in reminders:
    #             if days_left == 0:
    #                 print(f"• {event_name} - TODAY! ({event_date})")
    #             elif days_left == 1:
    #                 print(f"• {event_name} - TOMORROW! ({event_date})")
    #             else:
    #                 print(f"• {event_name} - in {days_left} days ({event_date})")
    #         print("=" * 50)
    #     else:
    #         print("\nNo upcoming events in the next 7 days.\n")
    # except Exception as e:
    #     print(f"Note: Could not check reminders: {e}")

    at_user_menu = True
    while at_user_menu:
        print(f"\n=== Welcome to the Ticket System, {username}! ===")
        print("1. View Available Events")
        print("2. Update User Details")
        print("3. View All Events")
        print("4. Inbox / Contact Admin")
        print("5. Logout")

        choice = input("Select an option (1-5): ")

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
                    # Check if user pressed "Back" in filter/sort menu
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
                        Tickets.purchase_ticket(username, event_choice, ticket_type,
                                                quantity)
                    else:
                        print("Quantity must be at least 1!")
                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "2":
            Users.update_user_details(username)

        elif choice == "3":
            all_events = Events.get_all_events()
            if all_events == "No events exist please create one":
                print("No events\n")
            else:
                at_user_menu = False
                view_all_events_menu(all_events, username)

        elif choice == "4":  # Inbox option
            show_inbox_menu(username)

        elif choice == "5":
            print("Logging out...")
            at_user_menu = False

        elif choice == "<-":
            print("Cannot go back from main menu")
        else:
            print("Invalid option! Please select 1-5.")


def view_all_events_menu(event_list, username):
    print("\n")
    event_index = 0
    for event in event_list:
        print(str(event_index + 1) + ". Event name: " + event["Event name"])
        print("\tStart date: " + event["Start date"])
        print("\tDescription: " + event["Description"] + "\n")
        event_index += 1

    at_events_menu = True
    while at_events_menu:
        user_input = input("Select an event or go back [1, 2, ..., <-]: ")
        if user_input == "<-":
            at_events_menu = False
            user_menu(username)
        elif int(user_input) <= event_index:
            # get event
            event = event_list[int(user_input) - 1]
            print(event["Event name"])
        else:
            print("No event of index", user_input)


# Simple messaging functions
MESSAGES_FILE = "questions.json"


def send_message_to_admin(username):
    """User sends a message to admin"""
    print("\n=== Send Message to Admin ===")
    message = input("Type your question (or [<-] to cancel): ")

    if message == "<-":
        return

    if not message.strip():
        print("Message cannot be empty!")
        return

    # Load or create messages file
    try:
        with open(MESSAGES_FILE, "r") as f:
            messages = json.load(f)
    except:
        messages = []

    # Add new message
    messages.append({
        "id": len(messages) + 1,
        "user": username,
        "question": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "answered": False
    })

    # Save
    with open(MESSAGES_FILE, "w") as f:
        json.dump(messages, f, indent=2)

    print("Message sent to admin!")


def view_my_messages(username):
# Users can view their messages
    try:
        with open(MESSAGES_FILE, "r") as f:
            all_messages = json.load(f)
    except:
        print("\nNo messages found.")
        return

    user_messages = [m for m in all_messages if m["user"] == username]

    if not user_messages:
        print("\nNo messages found.")
        return

    print(f"\n=== Your Messages ===")
    for msg in user_messages:
        print(f"\nQuestion: {msg['question']}")
        print(f"Date: {msg['timestamp']}")
        if msg["answered"] and "answer" in msg:
            print(f"Admin Response: {msg['answer']}")
        else:
            print("Status: Waiting for admin response")
    print()


def show_inbox_menu(username):
# Users inbox menu
    while True:
        print("\n=== Inbox / Contact Admin ===")
        print("1. Send Message to Admin")
        print("2. View My Messages")
        print("3. Back")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            send_message_to_admin(username)
        elif choice == "2":
            view_my_messages(username)
        elif choice == "3":
            break
        else:
            print("Invalid option!")


# Admin functions
def admin_login():
# Admin login
    print("\n=== ADMIN LOGIN ===")
    username = input("Admin Username: ")
    password = input("Password: ")

    return username == "Admin" and password == "1234"


def admin_view_questions():
# Admins can view aand reply to questions
    try:
        with open(MESSAGES_FILE, "r") as f:
            messages = json.load(f)
    except:
        print("\nNo questions found.")
        return

    unanswered = [m for m in messages if not m["answered"]]

    if not unanswered:
        print("\nNo unanswered questions.")
        return

    print(f"\n=== UNANSWERED QUESTIONS ({len(unanswered)}) ===")
    for msg in unanswered:
        print(f"\nID: {msg['id']}")
        print(f"From: {msg['user']}")
        print(f"Question: {msg['question']}")
        print(f"Time: {msg['timestamp']}")

    try:
        qid = int(input("\nEnter Question ID to reply (0 to skip): "))
        if qid > 0:
            answer = input("Your response: ")
            if answer.strip():
                for msg in messages:
                    if msg["id"] == qid:
                        msg["answered"] = True
                        msg["answer"] = answer
                        msg["answered_time"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                        break

                with open(MESSAGES_FILE, "w") as f:
                    json.dump(messages, f, indent=2)
                print("Response sent!")
    except:
        print("Invalid input.")


def admin_menu():
# Admin menu
    while True:
        print("\n=== ADMIN PANEL ===")
        print("1. View & Reply to Questions")
        print("2. Logout")

        choice = input("Select option (1-2): ")

        if choice == "1":
            admin_view_questions()
        elif choice == "2":
            print("Logging out...")
            break
        else:
            print("Invalid option!")


