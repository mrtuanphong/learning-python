import database

# Add a new record: ----------------
#database.add_one('Shiva', 'Hoang', 'shiva@gotitapp.co')

# Lookup with WHERE: ----------------
database.lookup_single_field('email', '\'phong@tutoruniverse.net\'')
database.lookup_single_field('rowid', '3')
database.lookup_single_field('first_name', '\'Thanh\'')

# Add many records: ----------------
# stuff = [
#   (
#     'Thang',
#     'Tran',
#     'thang@got-it.ai'
#   ),
#   (
#     'Thanh',
#     'Luong',
#     'thanh@got-it.ai'
#   ),
#   (
#     'Vu',
#     'Nguyen',
#     'vu@tutoruniverse.net'
#   ),
#   (
#     'Phong',
#     'Do',
#     'phong@tutoruniverse.net'
#   )
# ]
# database.add_many(stuff)

# Delete record use rowid as string: -----------------
# database.delete_one('6')


# Show all the records: ----------------
# database.show_all()