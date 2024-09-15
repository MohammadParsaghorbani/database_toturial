import sqlite3

conn = sqlite3.connect('ilia_data.db')
cursor = conn.cursor()

phone = input("phone: ")
id = input("id:")

a = cursor.execute("""
select price from book
where id = {}
""".format(id))
res = a.fetchall()
cursor.execute(f"""
insert into price_list values({phone},{id},'{res}')
""")

conn.commit()
conn.close()