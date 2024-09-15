import sqlite3

conn = sqlite3.connect('ilia_data.db')
cursor = conn.cursor()

cursor.execute("""
insert into book values(1,'mardi be name ove',250,350000)
""")

conn.commit()
conn.close()