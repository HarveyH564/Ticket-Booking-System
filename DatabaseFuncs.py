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


def initialise_db():
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        print("DB initialisation")

        # sqlite doesn't have foreign keys enabled by default must do this every connection
        enable_foreign_keys = "PRAGMA foreign_keys = ON;"

        venue_table_creation_query = """
CREATE TABLE IF NOT EXISTS Venues (
    venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    venue_name VARCHAR (30) NOT NULL,
    location VARCHAR (30) NOT NULL
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
    user_id INTEGER NOT NULL,
    price REAL,
    type VARCHAR (10),
    FOREIGN KEY (event_id) REFERENCES Events(event_id),
    FOREIGN KEY (seat_id) REFERENCES Seats(seat_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);"""

        #get_all_tables_query = "SELECT name FROM sqlite_master WHERE type='table';"

        cursor.execute(enable_foreign_keys)
        cursor.execute(venue_table_creation_query)
        cursor.execute(seats_table_creation_query)
        cursor.execute(events_table_creation_query)
        cursor.execute(users_table_creation_query)
        cursor.execute(tickets_table_creation_query)
        # cursor.execute(get_all_tables_query)

        result = cursor.fetchall()
        print("Tables: " + str(result))

        cursor.close()

    except sqlite3.Error as error:
        print("Error in DatabaseFuncs.initialise_db(): " + str(error))

    finally:
        if sqlite_connection:
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
        tables = ['Tickets', 'Users', 'Events', 'Seats', 'Venues']

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