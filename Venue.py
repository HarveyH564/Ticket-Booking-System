import sqlite3

# seat map should be structured [[["A1"], ["A2"], ["A3"]], [["B1"], ["B2"], ["B3"]]]
def create_venue(venue_name, location, seat_map):
    # TO DO
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        venue_creation_query = "INSERT INTO Venues(venue_name, location) VALUES ('" + venue_name + "', '" + location + "')"
        cursor.execute(venue_creation_query)
        get_venue_id_query = "SELECT venue_id FROM Venues WHERE venue_name = '" + venue_name + "' AND location = '" + location + "'"
        cursor.execute(get_venue_id_query)
        venue_id = cursor.fetchone()[0]

        for row in seat_map:
            for seat in row:
                populate_seats_query = "INSERT INTO Seats(seat_location, venue_id) VALUES ('" + str(seat[0]) + "', '" + str(venue_id) + "')"
                cursor.execute(populate_seats_query)

    except sqlite3.Error as error:
        print("Error: " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.commit()
            sqlite_connection.close()
    return

def get_all_venues():
    # TO DO
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        query = "SELECT * FROM Venues"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except sqlite3.Error as error:
        print("Error: " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.commit()
            sqlite_connection.close()

def delete_venue(id):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        query = "DELETE FROM Venues WHERE venue_id = '" + str(id) + "'"
        cursor.execute(query)

    except sqlite3.Error as error:
        print("Error: " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.commit()
            sqlite_connection.close()

def get_seats(venue_id):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("sql.db")
        cursor = sqlite_connection.cursor()
        query = "SELECT * FROM Seats WHERE venue_id = '" + str(venue_id) + "'"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except sqlite3.Error as error:
        print("Error: " + str(error))

    finally:
        if sqlite_connection:
            sqlite_connection.close()

class Venue():
    def __init__(self):
        self.seats = None
        self.location = None

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_seats(self, seats):
        self.seats = seats

    def get_seats(self):
        return self.seats

    def print_seats(self):
        for row in self.seats:
            row_list = ""
            for seat in row:
                row_list += str(seat)
            print(row_list)

    def __str__(self):
        return self.location

print(get_all_venues())
print(get_seats(8))