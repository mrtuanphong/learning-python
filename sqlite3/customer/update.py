import sqlite3

# Connect to database:
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Update records
c.execute("""UPDATE customers 
  SET 
    first_name = 'Lex',
    last_name = 'Nguyen',
    email = 'lex@gotitapp.co'
  WHERE
    last_name = '-'
""")

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