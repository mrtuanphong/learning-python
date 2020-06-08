import sqlite3

# Connect to database:
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Delete records
c.execute("DELETE FROM customers WHERE first_name='John'")

# Commit our command
conn.commit()

# Query the database
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
  print(item)

# Commit our command
conn.commit()

# Close our connection
conn.close()