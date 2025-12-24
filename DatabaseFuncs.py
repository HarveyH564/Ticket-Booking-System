import sqlite3

# This function is a skeleton for writing other functions to do with sqlite
'''
def db_connection_skeleton():
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        # sqlite doesn't have foreign keys enabled by default must do this every connection
        enable_foreign_keys = "PRAGMA foreign_keys = ON;"
        query = ""
        cursor.execute(enable_foreign_keys)
        cursor.execute(query)
        result = cursor.fetchall()


    except sqlite3.Error as error:
        print("Error: " + str(error))

    finally:
        if sqlite_connection:
            !!! IF YOU ARE UPDATING, INSERTING OR DELETING USE sqlite_connection.commit()
            sqlite_connection.close()
'''

# Table creation queries
venue_table_creation_query = """
CREATE TABLE IF NOT EXISTS Venues (
    venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    venue_name VARCHAR (30) NOT NULL,
    location VARCHAR (30) NOT NULL,
    UNIQUE (venue_name, location)  
);"""

seats_table_creation_query = """
CREATE TABLE IF NOT EXISTS Seats (
    seat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    seat_location VARCHAR (5),
    venue_id INTEGER NOT NULL,
    UNIQUE (seat_location, venue_id),
    FOREIGN KEY (venue_id) REFERENCES Venues(venue_id)
);"""

events_table_creation_query = """    
CREATE TABLE IF NOT EXISTS Events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name VARCHAR (50) NOT NULL,
    venue_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    description VARCHAR(255),
    UNIQUE (event_name, venue_id, start_date),
    FOREIGN KEY (venue_id) REFERENCES Venues(venue_id)
);"""

users_table_creation_query = """
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(15) UNIQUE NOT NULL,
    password VARCHAR(15) NOT NULL
);"""

tickets_table_creation_query = """
CREATE TABLE IF NOT EXISTS Tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    seat_id INTEGER NOT NULL,
    user_id INTEGER,
    price REAL,
    type VARCHAR (10),
    FOREIGN KEY (event_id) REFERENCES Events(event_id),
    FOREIGN KEY (seat_id) REFERENCES Seats(seat_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);"""

cart_table_creation_query = """
CREATE TABLE IF NOT EXISTS Cart (
    cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    UNIQUE (user_id, event_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);"""

# Populate venues table with 2 sample venues and the seats table for a sample list for each event
def init_populate_venues(cursor):
    insert_venues_query_1 = "INSERT INTO Venues(venue_name, location) VALUES ('O2 academy', 'Leicester');"
    insert_venues_query_2 = "INSERT INTO Venues(venue_name, location) VALUES ('Thekla', 'Bristol');"
    cursor.execute(insert_venues_query_1)
    cursor.execute(insert_venues_query_2)

    # seat ids are needed for ticket creation
    venue_1_seat_ids = []
    venue_2_seat_ids = []
    seat_map = [[["A1"], ["A2"], ["A3"]], [["B1"], ["B2"], ["B3"]]]

    venue_1_id_query = "SELECT venue_id FROM Venues WHERE venue_name = 'O2 academy' AND location = 'Leicester';"
    cursor.execute(venue_1_id_query)
    venue_1_id = cursor.fetchone()[0]
    for row in seat_map:
        for seat in row:
            populate_seats_query = "INSERT INTO Seats(seat_location, venue_id) VALUES ('" + str(seat[0]) + "', '" + str(venue_1_id) + "');"
            cursor.execute(populate_seats_query)
            get_seat_id = "SELECT seat_id FROM Seats WHERE seat_location = '" + str(seat[0]) + "' AND venue_id = '" + str(venue_1_id) + "';"
            cursor.execute(get_seat_id)
            seat_id = cursor.fetchone()[0]
            venue_1_seat_ids.append(seat_id)

    venue_2_id_query = "SELECT venue_id FROM Venues WHERE venue_name = 'Thekla' AND location = 'Bristol';"
    cursor.execute(venue_2_id_query)
    venue_2_id = cursor.fetchone()[0]
    for row in seat_map:
        for seat in row:
            populate_seats_query = "INSERT INTO Seats(seat_location, venue_id) VALUES ('" + str(seat[0]) + "', '" + str(venue_2_id) + "');"
            cursor.execute(populate_seats_query)
            get_seat_id = "SELECT seat_id FROM Seats WHERE seat_location = '" + str(seat[0]) + "' AND venue_id = '" + str(venue_2_id) + "';"
            cursor.execute(get_seat_id)
            seat_id = cursor.fetchone()[0]
            venue_2_seat_ids.append(seat_id)

    return [venue_1_id, venue_2_id, venue_1_seat_ids, venue_2_seat_ids]

# Populate events table with 2 sample events (1 for each sample venue)
def init_populate_events(cursor, venue_1_id, venue_2_id):

    insert_events_query_1 = "INSERT INTO Events(event_name, venue_id, start_date, end_date, description) VALUES ('Halloween Party', " + str(venue_1_id) + ", '2025-10-31', '2025-11-01', 'Leicester Halloween Party at the O2');"
    cursor.execute(insert_events_query_1)


    insert_events_query_2 = "INSERT INTO Events(event_name, venue_id, start_date, end_date, description) VALUES ('Christmas Party', " + str(venue_2_id) + ", '2025-12-20', '2025-12-21', 'Bristol Christmas Party at the O2');"
    cursor.execute(insert_events_query_2)


# Populate tickets table with tickets for each sample seat in sample each event
def init_populate_tickets(cursor, venue_1_id, venue_2_id, venue_1_seat_ids, venue_2_seat_ids):
    event_1_id_query = "SELECT event_id FROM Events WHERE event_name = 'Halloween Party' AND venue_id = " + str(venue_1_id) + " AND start_date = '2025-10-31';"
    cursor.execute(event_1_id_query)
    event_1_id = cursor.fetchone()[0]

    event_2_id_query = "SELECT event_id FROM Events WHERE event_name = 'Christmas Party' AND venue_id = " + str(venue_2_id) + " AND start_date = '2025-12-20';"
    cursor.execute(event_2_id_query)
    event_2_id = cursor.fetchone()[0]

    for seat in venue_1_seat_ids:
        insert_tickets_query_1 = "INSERT INTO Tickets(event_id, seat_id, user_id) VALUES (" + str(event_1_id) + ", " + str(seat) + ", NULL);"
        cursor.execute(insert_tickets_query_1)

    for seat in venue_2_seat_ids:
        insert_tickets_query_2 = "INSERT INTO Tickets(event_id, seat_id, user_id) VALUES ('" + str(event_2_id) + "', '" + str(seat) + "', NULL);"
        cursor.execute(insert_tickets_query_2)

def initialise_db():
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        print("DB initialisation")

        # sqlite doesn't have foreign keys enabled by default must do this every connection
        enable_foreign_keys = "PRAGMA foreign_keys = ON;"

        # Create tables
        cursor.execute(enable_foreign_keys)
        cursor.execute(venue_table_creation_query)
        cursor.execute(seats_table_creation_query)
        cursor.execute(events_table_creation_query)
        cursor.execute(users_table_creation_query)
        cursor.execute(tickets_table_creation_query)
        cursor.execute(cart_table_creation_query)

        # If there's no venues add 2
        get_venues_query = "SELECT * FROM Venues;"
        cursor.execute(get_venues_query)
        venues = cursor.fetchone()
        venue_1_id = None
        venue_2_id = None
        venue_1_seat_ids = []
        venue_2_seat_ids = []
        if not venues:
            venue_data = init_populate_venues(cursor)
            venue_1_id = venue_data[0]
            venue_2_id = venue_data[1]
            venue_1_seat_ids = venue_data[2]
            venue_2_seat_ids = venue_data[3]

        # If there's no events add 2 (1 per venue) and populate their seats (2 rows of seats, each with 3 seats)
        get_events_query = "SELECT * FROM Events;"
        cursor.execute(get_events_query)
        events = cursor.fetchone()
        if not events:
            init_populate_events(cursor, venue_1_id, venue_2_id)

        # If there's no tickets create them for the events
        get_tickets_query = "SELECT * FROM Tickets;"
        cursor.execute(get_tickets_query)
        tickets = cursor.fetchone()
        if not tickets:
            init_populate_tickets(cursor, venue_1_id, venue_2_id, venue_1_seat_ids, venue_2_seat_ids)


        cursor.close()

    except sqlite3.Error as error:
        print("Error in DatabaseFuncs.initialise_db(): " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.commit()
            sqlite_connection.close()

    return

def get_all_tables():
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        # sqlite doesn't have foreign keys enabled by default must do this every connection
        enable_foreign_keys = "PRAGMA foreign_keys = ON;"
        get_all_tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(enable_foreign_keys)
        cursor.execute(get_all_tables_query)
        result = cursor.fetchall()
        return result


    except sqlite3.Error as error:
        print("Error: " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.close()

def delete_all_tables():
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        enable_foreign_keys = "PRAGMA foreign_keys = ON;"
        get_all_tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(enable_foreign_keys)
        cursor.execute(get_all_tables_query)
        tables = ['Cart', 'Tickets', 'Users', 'Events', 'Seats', 'Venues']

        for table in tables:
            drop_query = "DROP TABLE IF EXISTS " + table + ";"
            cursor.execute(drop_query)

        # drop id increment to reset it
        drop_query = "DELETE FROM sqlite_sequence;"
        cursor.execute(drop_query)

        print("Tables dropped")

    except sqlite3.Error as error:
        print("Error: " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.commit()
            sqlite_connection.close()