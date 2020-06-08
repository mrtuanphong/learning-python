import sqlite3

# Connect to database:
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Insert data
c.execute("""INSERT INTO customers VALUES (
    'John',
    'Elder',
    'john@codemy.com'
  )""")

# Or write the command in 1 line:
# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")

print("Command executed succesfully!")

# Commit our command
conn.commit()

# Close our connection
conn.close()