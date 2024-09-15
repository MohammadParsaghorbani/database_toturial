import sqlite3

conn = sqlite3.connect('ilia_data.db')
cursor = conn.cursor()

name = input("enter name: ")

cursor.execute("""
select * from users
where name = '{}'
""".format(name))
res = cursor.fetchall()
print(res)

conn.commit()
conn.close()