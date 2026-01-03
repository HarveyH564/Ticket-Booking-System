import json
import os


class Venue():
    def __init__(self, location="", rows=5, cols=5):
        self.location = location
        self.rows = rows
        self.cols = cols
        # Create seat map: O = available, X = occupied
        self.seats = [["O" for _ in range(cols)] for _ in range(rows)]

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def get_seats(self):
        return self.seats

    def print_seats(self):
        print(f"\nSeating Map for {self.location} ({self.rows}x{self.cols}):")
        print("   " + " ".join(str(i + 1).rjust(2) for i in range(self.cols)))
        for i, row in enumerate(self.seats):
            print(f"{chr(65 + i)} | " + " ".join(f" {seat}" for seat in row))
        print()

    def __str__(self):
        return f"Venue: {self.location}, Size: {self.rows}x{self.cols}, Total seats: {self.rows * self.cols}"


# Venue management functions

VENUES_FILE = "venues.json"


def load_venues():
    # Get venues from JSON
    if not os.path.exists(VENUES_FILE):
        return []

    try:
        with open(VENUES_FILE, 'r') as f:
            venues_data = json.load(f)

        venues = []
        for venue_data in venues_data:
            venue = Venue(
                venue_data["location"],
                venue_data["rows"],
                venue_data["cols"]
            )
            venues.append(venue)
        return venues
    except:
        return []


def save_venues(venues):
    # Save venues to JSON
    venues_data = []
    for venue in venues:
        venues_data.append({
            "location": venue.location,
            "rows": venue.rows,
            "cols": venue.cols,
            "seats": venue.seats
        })

    with open(VENUES_FILE, 'w') as f:
        json.dump(venues_data, f, indent=2)


def add_venue(location, rows=5, cols=5):
    # Add new venue and its size
    venues = load_venues()

    # Validate inputs
    if not location:
        return False, "Venue name cannot be empty"

    try:
        rows = int(rows)
        cols = int(cols)
        if rows <= 0 or cols <= 0:
            return False, "Rows and columns must be positive numbers"
        if rows > 20 or cols > 30:
            return False, "Maximum size is 20x30"
    except ValueError:
        return False, "Rows and columns must be numbers"

    # Check if venue already exists
    for venue in venues:
        if venue.location.lower() == location.lower():
            return False, "Venue already exists"

    # Create new venue
    new_venue = Venue(location, rows, cols)
    venues.append(new_venue)
    save_venues(venues)
    return True, f"Venue '{location}' added successfully ({rows}x{cols})"


def update_venue(old_location, new_location, new_rows=None, new_cols=None):

    venues = load_venues()

    # Find venue
    for venue in venues:
        if venue.location.lower() == old_location.lower():
            # Check if new location already exists
            if new_location and new_location.lower() != old_location.lower():
                for v in venues:
                    if v.location.lower() == new_location.lower():
                        return False, "New location already exists"
                venue.location = new_location

            # Update size if provided
            if new_rows is not None:
                try:
                    rows = int(new_rows)
                    if rows <= 0:
                        return False, "Rows must be positive"
                    venue.rows = rows
                    # Resize seats
                    venue.seats = [["O" for _ in range(venue.cols)] for _ in range(rows)]
                except ValueError:
                    return False, "Rows must be a number"

            if new_cols is not None:
                try:
                    cols = int(new_cols)
                    if cols <= 0:
                        return False, "Columns must be positive"
                    venue.cols = cols
                    # Resize seats
                    venue.seats = [["O" for _ in range(cols)] for _ in range(venue.rows)]
                except ValueError:
                    return False, "Columns must be a number"

            save_venues(venues)
            return True, f"Venue updated to '{venue.location}' ({venue.rows}x{venue.cols})"

    return False, "Venue not found"


def delete_venue(location):
    # Delete a venue
    venues = load_venues()

    # Find and remove venue
    for i, venue in enumerate(venues):
        if venue.location.lower() == location.lower():
            del venues[i]
            save_venues(venues)
            return True, f"Venue '{location}' deleted"

    return False, "Venue not found"


def list_venues():
    # Get all venues
    venues = load_venues()
    return venues


def get_venue(location):
    # Get spesific venues
    venues = load_venues()
    for venue in venues:
        if venue.location.lower() == location.lower():
            return venue
    return None


def resize_venue(location, rows, cols):
    # Resize venues
    venues = load_venues()

    for venue in venues:
        if venue.location.lower() == location.lower():
            try:
                rows = int(rows)
                cols = int(cols)
                if rows <= 0 or cols <= 0:
                    return False, "Rows and columns must be positive"

                venue.rows = rows
                venue.cols = cols
                venue.seats = [["O" for _ in range(cols)] for _ in range(rows)]
                save_venues(venues)
                return True, f"Venue resized to {rows}x{cols}"
            except ValueError:
                return False, "Rows and columns must be numbers"

    return False, "Venue not found"