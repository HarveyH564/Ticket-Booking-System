import json
import os
import sqlite3

def create_user():
    return


def delete_user():
    return


def update_user():
    return

def create_account():
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        enable_foreign_keys = "PRAGMA foreign_keys = ON;"
        cursor.execute(enable_foreign_keys)
        invalid_username = True
        while invalid_username:
            username = input("Enter username: ")
            if username == "<-":
                print()
                return [False, False]
            else:
                query = "SELECT * FROM Users WHERE Username='" + username + "';"
                cursor.execute(query)
                result = cursor.fetchone()
                if result:
                    print("User already exists")
                else:
                    password = input("Enter password: ")
                    if password == "<-":
                        return [False, False]
                    else:
                        query = "INSERT INTO Users(username, password) VALUES('" + username + "', '" + password + "');"
                        cursor.execute(query)
                        print("Account creation successful")
                        return [True, username]

    except sqlite3.Error as error:
        print("Error in Users.create_account(): " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.commit()
            sqlite_connection.close()

def login():
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        enable_foreign_keys = "PRAGMA foreign_keys = ON;"
        cursor.execute(enable_foreign_keys)

        incorrect_username = True
        incorrect_password = None
        while incorrect_username:
            username = input("Enter username: ")
            if username == "<-":
                return [False, False]

            else:
                query = "SELECT * FROM Users WHERE Username='" + username + "';"
                cursor.execute(query)
                result = cursor.fetchall()
                if result:
                    # break loop
                    incorrect_username = False
                    incorrect_password = True

                    # new loop
                    while incorrect_password:
                        password_attempt = input("Enter password: ")
                        if password_attempt == "<-":
                            return [False, False]
                        elif password_attempt == result[0][2]:
                            incorrect_password = False
                            print("Login successful")
                            return [True, username]
                        else:
                            print("Incorrect password, please try again")


                else:
                    print("User doesn't exist, please try again")

    except sqlite3.Error as error:
        print("Error in Users.login(): " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.close()

def get_user(username):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        enable_foreign_keys = "PRAGMA foreign_keys = ON;"
        query = "SELECT * FROM Users WHERE Username='" + username + "';"
        cursor.execute(enable_foreign_keys)
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(result[0][1])
        else:
            print("No such user")

    except sqlite3.Error as error:
        print("Error in Users.get_user(): " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.close()

def get_all_users():
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        enable_foreign_keys = "PRAGMA foreign_keys = ON;"
        query = "SELECT * FROM Users;"
        cursor.execute(enable_foreign_keys)
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            return result
        else:
            print("No users")

    except sqlite3.Error as error:
        print("Error in Users.get_all_users(): " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.close()


class User():
    def __init__(self):
        self.username = None
        self.password = None
        self.purchased_tickets = None
        self.cart = None

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_purchased_tickets(self, purchased_tickets):
        self.purchased_tickets = purchased_tickets

    def get_purchased_tickets(self):
        return self.purchased_tickets

    def set_cart(self, cart):
        self.cart = cart

    def add_to_cart(self, ticket):
        self.cart.append(ticket)

    def remove_from_cart(self, ticket):
        self.cart.remove(ticket)

    def get_cart(self):
        return self.cart

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