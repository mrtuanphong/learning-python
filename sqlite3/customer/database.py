import sqlite3

# Query the DB and return all records:
# ------------------------------------
def show_all():
  conn = sqlite3.connect("customer.db")
  c = conn.cursor()
  c.execute("SELECT rowid, * FROM customers")
  items = c.fetchall()
  for item in items:
    print(item)
  conn.commit()
  conn.close()

# Lookup with WHERE:
# ------------------------------------
def lookup_single_field(field, value):
  conn = sqlite3.connect("customer.db")
  c = conn.cursor()
  #cmd = "SELECT rowid, * FROM customers WHERE " + field + " = " + value
  #print(cmd)
  c.execute("SELECT rowid, * FROM customers WHERE " + field + " = " + value)
  items = c.fetchall()
  for item in items:
    print(item)
  conn.commit()
  conn.close()

# Add a new record to the table:
# ------------------------------
def add_one(first_name, last_name, email):
  conn = sqlite3.connect("customer.db")
  c = conn.cursor()
  c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first_name, last_name, email))
  conn.commit()
  conn.close()

# Add many records to the table:
# ------------------------------
def add_many(list):
  conn = sqlite3.connect("customer.db")
  c = conn.cursor()
  c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (list))
  conn.commit()
  conn.close()

# Delete a record from the table
# by using rowid as a string:
# ------------------------------
def delete_one(id):
  conn = sqlite3.connect("customer.db")
  c = conn.cursor()
  c.execute("DELETE FROM customers WHERE rowid = (?)", (id))
  conn.commit()
  conn.close()
