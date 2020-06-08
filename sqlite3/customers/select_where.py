import sqlite3

# Connect to database:
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%gotitapp%'")
items = c.fetchall()
for item in items:
  print(item)

# Commit our command
conn.commit()

# Close our connection
conn.close()