"""Create a SQLite3 database and table"""
import sqlite3

# Connect to the DB
conn = sqlite3.connect("new.db")

# Obtain a cursor
cursor = conn.cursor()

# Create the table "population", if still does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS popuplation(city TEXT, state TEXT, population INTEGER)")

#close the connection