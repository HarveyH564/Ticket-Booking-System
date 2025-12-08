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
