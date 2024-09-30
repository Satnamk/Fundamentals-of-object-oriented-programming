# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.

import sqlite3
from geopy.distance import geodesic

def fetch_airport_coordinates(icao_code):
    # Connect to the SQLite database
    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()

    # Query to fetch airport coordinates based on ICAO code
    cursor.execute("SELECT latitude, longitude FROM airports WHERE ident = ?", (icao_code,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    if result:
        return result  # Returns (latitude, longitude)
    else:
        return None  # ICAO code not found

def main():
    icao_code1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao_code2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    # Fetch coordinates for both airports
    coords1 = fetch_airport_coordinates(icao_code1)
    coords2 = fetch_airport_coordinates(icao_code2)

    if coords1 and coords2:
        # Calculate the distance between the two airports
        distance = geodesic(coords1, coords2).kilometers
        print(f"The distance between {icao_code1} and {icao_code2} is {distance:.2f} kilometers.")
    else:
        if not coords1:
            print(f"ICAO code '{icao_code1}' not found.")
        if not coords2:
            print(f"ICAO code '{icao_code2}' not found.")

# Run the main program
if __name__ == "__main__":
    main()
