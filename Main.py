import Menus
import DatabaseFuncs as db

def main():
    db.initialise_db()

    print("=== Simple Ticket System ===")
    logged_in = [False, False]
    while not logged_in[0]:
        logged_in = Menus.initial_menu()

    if logged_in[0]:
        Menus.user_menu(logged_in[1])


if __name__ == "__main__":
    main()
#("All Venues: ", Venues.get_all_venues())
#print("Venue 1 Seats: ", Venues.get_seats_for_venue(1))
#print("All Events: ", Events.get_all_events())
#print("Event 1 Tickets: ", Events.get_ti  ckets_for_event(1))