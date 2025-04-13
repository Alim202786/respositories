import psycopg2
import csv
import os

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="postgres",     
        user="postgres",
        password="alim_788607131523",  
        client_encoding="UTF8"
    )

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
    print("Таблица готова!")

def insert_manual():
    conn = connect()
    cur = conn.cursor()
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name.strip(), phone.strip()))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные добавлены.")

def insert_from_csv():
    conn = connect()
    cur = conn.cursor()
    file_name = input("Введите имя CSV-файла (например, contacts.csv): ").strip()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, file_name)
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print("Прочитано из CSV:", row)
                if len(row) == 2:
                    name, phone = row
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name.strip(), phone.strip()))
        conn.commit()
        print("Данные из CSV успешно добавлены.")
    except FileNotFoundError:
        print("Файл не найден. Проверьте имя файла.")
    cur.close()
    conn.close()

def update_data():
    conn = connect()
    cur = conn.cursor()
    name = input("Чьё имя вы хотите изменить: ")
    new_phone = input("Новый номер телефона: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone.strip(), name.strip()))
    conn.commit()
    cur.close()
    conn.close()
    print("Номер обновлён.")

def query_data():
    conn = connect()
    cur = conn.cursor()
    name_filter = input("Введите имя для поиска: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name_filter.strip()}%",))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    if not rows:
        print("Ничего не найдено.")
    cur.close()
    conn.close()

def delete_data():
    conn = connect()
    cur = conn.cursor()
    name = input("Введите имя для удаления: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name.strip(),))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные удалены.")

def menu():
    create_table()
    while True:
        print("\nMENU PHONEBOOK:")
        print("1. Добавить данные вручную")
        print("2. Добавить данные из CSV-файла")
        print("3. Обновить номер телефона")
        print("4. Найти данные")
        print("5. Удалить данные")
        print("0. Выйти")

        choice = input("Выберите действие: ")
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
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()