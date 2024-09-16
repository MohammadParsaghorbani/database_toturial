import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# cursor.execute("""
# create table if not exists price_list(
#     phone int references users(phone),
#     book int references book(id),
#     price int
# )
# """)

# cursor.execute("""
# create table if not exists users(
#     phone int primary key,
#     name text,
#     last_name text
# )
# """)


connection.commit()
connection.close()