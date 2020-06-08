import sqlite3

# Connect to database:
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Drop table
c.execute("DROP TABLE table_name_here")

# Commit our command
conn.commit()

# Close our connection
conn.close()