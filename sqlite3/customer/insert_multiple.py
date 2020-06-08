import sqlite3

# Connect to database:
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Data
many_customers = [
  (
    'Phong',
    'Do',
    'phong@got-it.ai'
  ),
  (
    'Kyle',
    'Vu',
    'kyle@gotitapp.co'
  ),
  (
    'Jess',
    '-',
    'jess@gotitapp.co'
  ),
  (
    'Aaron',
    'Doan',
    'aaron@gotitapp.co'
  )
]

# Insert data
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

print("Command executed succesfully!")

# Commit our command
conn.commit()

# Close our connection
conn.close()