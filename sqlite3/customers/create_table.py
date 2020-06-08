import sqlite3

# Connect to database:
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE customers (
    first_name DATATYPE,
    last_name DATATYPE,
    email DATATYPE
  )""")

print("The table was created succesfully!")

# Commit our command
conn.commit()

# Close our connection
conn.close()