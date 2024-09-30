# Write a program that asks the user to enter the area code (for example FI) and
# prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.

import sqlite3
from collections import defaultdict

def fetch_airports_by_area_code(area_code):
    # Connect to the SQLite database
    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()

    # Query to fetch airport information based on area code
    cursor.execute("SELECT airport_type, name FROM airports WHERE area_code = ?", (area_code,))
    results = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Organize results by airport type
    airport_dict = defaultdict(list)
    for airport_type, name in results:
        airport_dict[airport_type].append(name)

    # Print the results
    if airport_dict:
        print(f"\nAirports in country code '{area_code}':")
        for airport_type in sorted(airport_dict.keys()):
            airport_count = len(airport_dict[airport_type])
            print(f"{airport_count} {airport_type} airport(s):")
            for name in airport_dict[airport_type]:
                print(f" - {name}")
    else:
        print(f"No airports found for the area code '{area_code}'.")

def main():
    area_code = input("Enter the area code (e.g., FI for Finland): ").strip().upper()
    fetch_airports_by_area_code(area_code)

# Run the main program
if __name__ == "__main__":
    main()
