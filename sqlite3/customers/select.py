import sqlite3

# Connect to database:
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT rowid, * FROM customers")

#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

items = c.fetchall()

#print(items)

for item in items:
  print(item)
  #print(item[0], '\t', item[1], '\t', item[2])

# Commit our command
conn.commit()

# Close our connection
conn.close()