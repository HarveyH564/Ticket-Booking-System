import json
import os
import sqlite3


import json
import os

def create_account():
    invalid_username = True
    while invalid_username:
        username = input("Enter username: ")
        if username == "<-":
            print()
            return [False, False]

        if os.path.exists("users/" + username + ".json"):
            print("Username is taken, please try again")
        else:
            user_file = open("users/" + username + ".json", "x")
            password = input("Enter password: ")
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

def login():
    incorrect_username = True
    while incorrect_username:
        username = input("Enter username: ")
        if username == "<-":
            print()
            return [False, False]

        if not os.path.exists("users/" + username + ".json"):
            print("User doesn't exist, please try again")
        else:
            incorrect_username = False
            incorrect_password = True
            user_file = open("users/" + username + ".json", "r")
            user_info = json.load(user_file)
            user_password = user_info["password"]

            while incorrect_password:
                password_attempt = input("Enter password: ")
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



# # returns [x,y] if account created x = True, y = userID. else x = False, y = False
# def create_account():
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         cursor.execute(enable_foreign_keys)
#         invalid_username = True
#         while invalid_username:
#             username = input("Enter username: ")
#             if username == "<-":
#                 print()
#                 return [False, False]
#             else:
#                 get_user_query = "SELECT * FROM Users WHERE Username='" + username + "';"
#                 cursor.execute(get_user_query)
#                 result = cursor.fetchone()
#                 if result:
#                     print("User already exists")
#                 else:
#                     password = input("Enter password: ")
#                     if password == "<-":
#                         return [False, False]
#                     else:
#                         add_user_query = "INSERT INTO Users(username, password) VALUES('" + username + "', '" + password + "');"
#                         cursor.execute(add_user_query)
#                         user_id_query = "SELECT user_id FROM Users WHERE username = '" + username + "';"
#                         cursor.execute(user_id_query)
#                         user_id = cursor.fetchone()[0]
#                         print("Account creation successful")
#                         return [True, user_id]
#
#     except sqlite3.Error as error:
#         print("Error in Users.create_account(): " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.commit()
#             sqlite_connection.close()
#
#
# def login():
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         cursor.execute(enable_foreign_keys)
#
#         incorrect_username = True
#         incorrect_password = None
#         while incorrect_username:
#             username = input("Enter username: ")
#             if username == "<-":
#                 return [False, False]
#
#             else:
#                 get_user_query = "SELECT * FROM Users WHERE Username='" + username + "';"
#                 cursor.execute(get_user_query)
#                 result = cursor.fetchall()
#                 if result:
#                     # break loop
#                     incorrect_username = False
#                     incorrect_password = True
#
#                     # new loop
#                     while incorrect_password:
#                         password_attempt = input("Enter password: ")
#                         if password_attempt == "<-":
#                             return [False, False]
#                         elif password_attempt == result[0][2]:
#                             incorrect_password = False
#                             user_id_query = "SELECT user_id FROM Users WHERE username = '" + username + "';"
#                             cursor.execute(user_id_query)
#                             user_id = cursor.fetchone()[0]
#                             print("Login successful")
#                             return [True, user_id]
#                         else:
#                             print("Incorrect password, please try again")
#
#
#                 else:
#                     print("User doesn't exist, please try again")
#
#     except sqlite3.Error as error:
#         print("Error in Users.login(): " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#
# # Func for testing
# def get_user(username):
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         query = "SELECT * FROM Users WHERE Username='" + username + "';"
#         cursor.execute(enable_foreign_keys)
#         cursor.execute(query)
#         result = cursor.fetchall()
#         if result:
#             print(result[0][1])
#         else:
#             print("No such user")
#
#     except sqlite3.Error as error:
#         print("Error in Users.get_user(): " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#
# # Func for testing
# def get_all_users():
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         query = "SELECT * FROM Users;"
#         cursor.execute(enable_foreign_keys)
#         cursor.execute(query)
#         result = cursor.fetchall()
#         if result:
#             return result
#         else:
#             print("No users")
#
#     except sqlite3.Error as error:
#         print("Error in Users.get_all_users(): " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#
# def add_to_cart(username, event_id):
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         # sqlite doesn't have foreign keys enabled by default must do this every connection
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         get_user_id_query = "SELECT user_id FROM Users WHERE username = '" + username + "';"
#         cursor.execute(enable_foreign_keys)
#         cursor.execute(get_user_id_query)
#         user_id = cursor.fetchone()[0]
#         print("User id: " + str(user_id))
#         add_to_cart_query = "INSERT INTO Cart(user_id, event_id) VALUES (" + str(user_id) + ", " + str(event_id) + ");"
#         cursor.execute(add_to_cart_query)
#
#     except sqlite3.Error as error:
#         if str(error) == "UNIQUE constraint failed: Cart.user_id, Cart.event_id":
#             print("Event already added to basket")
#         else:
#             print("Error in Users.add_to_cart(): " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.commit()
#             sqlite_connection.close()
#
# def get_users_cart(user_id):
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         # sqlite doesn't have foreign keys enabled by default must do this every connection
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         get_user_cart_query = "SELECT * FROM Cart WHERE user_id = " + str(user_id) + ";"
#         cursor.execute(enable_foreign_keys)
#         cursor.execute(get_user_cart_query)
#         user_cart = cursor.fetchall()
#         return user_cart
#
#     except sqlite3.Error as error:
#         print("Error in Users.get_users_cart(): " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#
# def remove_event_from_cart(username, event_id):
#     sqlite_connection = None
#     try:
#         sqlite_connection = sqlite3.connect("sql.db")
#         cursor = sqlite_connection.cursor()
#         # sqlite doesn't have foreign keys enabled by default must do this every connection
#         enable_foreign_keys = "PRAGMA foreign_keys = ON;"
#         get_user_id_query = "SELECT user_id FROM Users WHERE username = '" + username + "';"
#         cursor.execute(enable_foreign_keys)
#         cursor.execute(get_user_id_query)
#         user_id = cursor.fetchone()[0]
#         remove_event_query = "DELETE FROM Cart WHERE user_id = " + str(user_id) + " AND event_id = " + str(event_id) + ";"
#         cursor.execute(remove_event_query)
#         result = cursor.fetchall()
#
#     except sqlite3.Error as error:
#         print("Error in Users.remove_event_from_cart(): " + str(error))
#
#     finally:
#         if sqlite_connection:
#             sqlite_connection.commit()
#             sqlite_connection.close()


# class User():
#     def __init__(self):
#         self.username = None
#         self.password = None
#         self.purchased_tickets = None
#         self.cart = None
#
#     def set_username(self, username):
#         self.username = username
#
#     def get_username(self):
#         return self.username
#
#     def set_password(self, password):
#         self.password = password
#
#     def get_password(self):
#         return self.password
#
#     def set_purchased_tickets(self, purchased_tickets):
#         self.purchased_tickets = purchased_tickets
#
#     def get_purchased_tickets(self):
#         return self.purchased_tickets
#
#     def set_cart(self, cart):
#         self.cart = cart
#
#     def add_to_cart(self, ticket):
#         self.cart.append(ticket)
#
#     def remove_from_cart(self, ticket):
#         self.cart.remove(ticket)
#
#     def get_cart(self):
#         return self.cart

# Update user details option
def update_details(self):

    print("\n=== Update Account Details ===")
    print("1. Change username")
    print("2. Change password")
    print("3. Back")

    choice = input("Select an option: ")

    # Load user file
    user_file = f"{USERS_DIR}/{self.username}.json"

    if not os.path.exists(user_file):
        print("Error: User file not found.")
        return self.username

    with open(user_file, "r") as f:
        data = json.load(f)
    # Update username option
    if choice == "1":
        new_username = input("Enter new username: ")

        if new_username.strip() == "":
            print("Username cannot be empty.")
            return self.username

        new_file = f"{USERS_DIR}/{new_username}.json"

        if os.path.exists(new_file):
            print("That username is already taken.")
            return self.username

        # Rename file
        os.rename(user_file, new_file)

        # Update stored username in JSON
        data["username"] = new_username

        with open(new_file, "w") as f:
            json.dump(data, f, indent=4)

        # Update in-memory value
        self.username = new_username

        print("Username updated successfully!")
        return new_username

        # Update password option
    elif choice == "2":
        new_password = input("Enter new password: ")

        if new_password.strip() == "":
            print("Password cannot be empty.")
            return self.username

        data["password"] = new_password

        with open(user_file, "w") as f:
            json.dump(data, f, indent=4)

        self.password = new_password

        print("Password updated successfully!")
        return self.username

        # Go back option
    else:
        return self.username

# Update details section
def update_user_details(username):
    user_file_path = f"users/{username}.json"
    if not os.path.exists(user_file_path):
        print("User file not found!")
        return

    with open(user_file_path, "r") as file:
        user_data = json.load(file)

    print("\n=== Update User Details ===")
    new_username = input(f"Enter new username (leave blank to keep '{user_data['username']}'): ")
    new_password = input("Enter new password (leave blank to keep current password): ")

    if new_username:
        new_user_file_path = f"users/{new_username}.json"
        if os.path.exists(new_user_file_path):
            print("Username already taken, please try again.")
            return
        os.rename(user_file_path, new_user_file_path)
        user_data["username"] = new_username
        username = new_username

    if new_password:
        user_data["password"] = new_password

    with open(f"users/{username}.json", "w") as file:
        json.dump(user_data, file)

    print("User details updated successfully!\n")


# ===== ADMIN USER MANAGEMENT HELPERS =====



USERS_DIR = "users"

def user_file(username):
    return os.path.join(USERS_DIR, f"{username}.json")

def user_exists(username):
    return os.path.exists(user_file(username))

def list_all_users():
    if not os.path.exists(USERS_DIR):
        return []
    return sorted(
        filename[:-5]
        for filename in os.listdir(USERS_DIR)
        if filename.endswith(".json")
    )

def load_user(username):
    if not user_exists(username):
        return None
    with open(user_file(username), "r") as f:
        return json.load(f)

def create_user(username, password):
    if not username or not password:
        return False
    if user_exists(username):
        return False

    data = {
        "username": username,
        "password": password,
        "tickets": {},
        "cart": {}
    }
    with open(user_file(username), "w") as f:
        json.dump(data, f, indent=4)
    return True

def delete_user(username):
    if not user_exists(username):
        return False
    os.remove(user_file(username))
    return True

def update_user(old_username, new_username, new_password):
    if not user_exists(old_username):
        return False

    if new_username != old_username and user_exists(new_username):
        return False

    data = load_user(old_username)
    data["username"] = new_username
    data["password"] = new_password

    old_path = user_file(old_username)
    new_path = user_file(new_username)

    if new_username != old_username:
        os.rename(old_path, new_path)

    with open(user_file(new_username), "w") as f:
        json.dump(data, f, indent=4)

    return True

def refund_event_tickets(event_name):
    if not os.path.exists(USERS_DIR):
        return 0

    updated = 0

    for file in os.listdir(USERS_DIR):
        if not file.endswith(".json"):
            continue

        path = os.path.join(USERS_DIR, file)
        with open(path, "r") as f:
            data = json.load(f)

        changed = False

        tickets = data.get("tickets", {})
        for key in list(tickets.keys()):
            if key.startswith(event_name + " -"):
                del tickets[key]
                changed = True
        data["tickets"] = tickets

        records = data.get("ticket_records", [])
        new_records = [r for r in records if not str(r.get("ticket", "")).startswith(event_name + " -")]
        if len(new_records) != len(records):
            data["ticket_records"] = new_records
            changed = True

        if changed:
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
            updated += 1

    return updated
