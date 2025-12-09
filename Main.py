import Menus
import DatabaseFuncs as db

def main():
    db.initialise_db()

    print("=== Simple Ticket System ===")
    logged_in = [False, False]
    while not logged_in[0]:
        logged_in = Menus.initial_menu()

    #if logged_in[0]:
    #    user_menu(logged_in[1])



if __name__ == "__main__":
    main()
