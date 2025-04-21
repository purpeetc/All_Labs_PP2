import psycopg2
import csv

#PostgreSQL-ге қосылу!
def connect():
    return psycopg2.connect(
        host="localhost",    # адрес сервера
        port=5432,             # порт
        dbname="mydb",       # имя базы данных
        user="myuser",       # имя пользователя
        password="mypassword" # пароль
    )

#Кесте жасау: create table
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Кесте дайын!")

#Деректерді енгізу орны: 
def insert_manual():
    conn = connect()
    cur = conn.cursor()
    name = input("Input your name: ")
    phone = input("Input your phone number: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("All informations added.")

#CSV файл арқылы енгізу
import os

def insert_from_csv():
    conn = connect()
    cur = conn.cursor()
    base_dir = os.path.dirname(__file__)
    filename = input("CSV file name (e.g. contacts.csv): ")
    file_path = os.path.join(base_dir, filename)

    if not os.path.exists(file_path):
        print(f" File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                name, phone = row
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (name, phone)
                )
    conn.commit()
    cur.close()
    conn.close()
    print(" Data loaded from CSV")

#Дерек жаңарту
def update_data():
    conn = connect()
    cur = conn.cursor()
    name = input("What kind of name do you want to change?")
    new_phone = input("New phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()
    print("Phone number updated")

#Дерек оқу (фильтрмен)
def query_data():
    conn = connect()
    cur = conn.cursor()
    name_filter = input("Input the name: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name_filter,))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone number: {row[2]}")
    if not rows:
        print("Nothing found")
    cur.close()
    conn.close()

#Дерек жою
def delete_data():
    conn = connect()
    cur = conn.cursor()
    name = input("What kind of name do you want to delete?")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("Information deleted")
    
#1-ші функция: pattern арқылы іздеу.
def search_by_pattern():
    conn = connect()
    cur = conn.cursor()
    pattern = input("Іздеу үшін сөз енгізіңіз (name немесе phone): ")
    
    # SQL-дің ішіндегі LIKE арқылы іздеу
    query = """
        SELECT * FROM phonebook
        WHERE name ILIKE %s OR phone ILIKE %s
    """
    like_pattern = f"%{pattern}%"
    cur.execute(query, (like_pattern, like_pattern))
    
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("Nothing found")
    
    cur.close()
    conn.close()


#Меню
def menu():
    create_table()  # Бірінші рет қосылғанда кесте жасап қояды
    while True:
        print("\n PHONEBOOK:")
        print("1. Adding information by myself")
        print("2. Adding informations from CSV file.")
        print("3. Updating informations.")
        print("4. Search the information")
        print("5. Delete information")
        print("6. Search by pattern")
        print("0. Exist")

        choice = input("Choose the option: ")
        if choice == "1":
            insert_manual()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            search_by_pattern()
        elif choice == "0":
            print("The code stopped. Thank you!")
            break
        else:
            print("ERROR. Please, try again.")

#Кодты іске қосу
if __name__ == "__main__":
    menu()
    
    
