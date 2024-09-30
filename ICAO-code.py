# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and
# location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.

import sqlite3

def fetch_airport_info(icao_code):
    # Connect to the SQLite database
    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()

    # Query to fetch airport information
    cursor.execute("SELECT name, location FROM airports WHERE ident = ?", (icao_code,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    if result:
        name, location = result
        print(f"Airport Name: {name}")
        print(f"Location: {location}")
    else:
        print("No airport found with the given ICAO code.")

def main():
    icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
    fetch_airport_info(icao_code)

# Run the main program
if __name__ == "__main__":
    main()
