import streamlit as st
import sqlite3

st.title("Plate Number Lookup")

# Connect to your online or local database
conn = sqlite3.connect('locations.db')  # Use a path or remote DB if hosted online
cursor = conn.cursor()

plate_number = st.text_input("Enter Plate Number (or part):")

if plate_number:
    query = "SELECT * FROM locations WHERE Plate_Number LIKE ?"
    cursor.execute(query, ('%' + plate_number + '%',))
    results = cursor.fetchall()

    if results:
        for row in results:
            st.write(f"**Location:** {row[0]}")
            st.write(f"**Plate Number:** {row[1]}")
            st.write(f"**Description (Arabic):** {row[2]}")
            st.write(f"**Description (English):** {row[3]}")
            st.write(f"**Available Rooms:** {row[4]}")
            st.write("---")
    else:
        st.write("No results found.")
