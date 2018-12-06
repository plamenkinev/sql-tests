""" Creates a cars.db with car inventory"""

# importing the module
import sqlite3

# create/ connect to a database
conn = sqlite3.connect("cars.db")

# obtain a cursor
cursor = conn.cursor()

# create a table inventory
cursor.execute("CREATE TABLE IF NOT EXISTS inventory(make TEXT, model TEXT, quantity INTEGER)")

# close the connections
conn.close()