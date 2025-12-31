import Menus


def main():

    print("=== Simple Ticket System ===")

    while True:
        print("\n=== MAIN MENU ===")
        print("1. User Login / Create Account")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            logged_in = Menus.initial_menu()
            if logged_in[0]:
                Menus.user_menu(logged_in[1])

        elif choice == "2":
            if Menus.admin_login():
                Menus.admin_menu()
            else:
                print("Invalid admin credentials!")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
#("All Venues: ", Venues.get_all_venues())
#print("Venue 1 Seats: ", Venues.get_seats_for_venue(1))
#print("All Events: ", Events.get_all_events())
#print("Event 1 Tickets: ", Events.get_tickets_for_event(1))