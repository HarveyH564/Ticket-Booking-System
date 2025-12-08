import os
import json

USERS_DIR = "users"


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
