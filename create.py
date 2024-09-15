import sqlite3

connection = sqlite3.connect('ilia_data.db')
cursor = connection.cursor()

cursor.execute("""
create table if not exists price_list(
    phone int references users(phone),
    book int references book(id),
    price int
)
""")

connection.commit()
connection.close()