import sqlite3


while True:
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    choice = input("options:\n\t1) enter\n\t2) exit\n")
    if choice == "1":
        phone = int(input("enter your phone_number: "))
        name = str(input("enter your name: "))
        last_name = str(input("enter your last name: "))

        cursor.execute(f"""
        insert into users values({phone},'{name}','{last_name}')
        """)
    elif choice == "2":
        break
    connection.commit()

    connection.close()
