import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="alim_788607131523",
    client_encoding="UTF8"
)
cur = conn.cursor()

def add_or_update_user():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("CALL add_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    print("Пользователь добавлен или обновлён")

def search_by_pattern():
    pattern = input("Введите шаблон для поиска: ")
    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Ничего не найдено")

def delete_user():
    value = input("Введите имя или номер телефона для удаления: ")
    cur.execute("CALL delete_user(%s);", (value,))
    conn.commit()
    print("Пользователь удалён")

def bulk_insert_from_csv():
    filename = input("Введите имя CSV-файла: ")
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            names = []
            phones = []
            for row in reader:
                if len(row) >= 2:
                    names.append(row[0])
                    phones.append(row[1])
            cur.execute("CALL bulk_insert_users(%s, %s, NULL);", (names, phones))
            conn.commit()
            print("Данные загружены")
    except FileNotFoundError:
        print("Файл не найден")

def get_paginated():
    limit = int(input("Сколько записей показать: "))
    offset = int(input("Сколько пропустить: "))
    cur.execute("SELECT * FROM get_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")

def menu():
    while True:
        print("\nPHONEBOOK MENU:")
        print("1. Добавить или обновить пользователя ")
        print("2. Поиск по шаблону ")
        print("3. Удалить по имени или номеру")
        print("4. Массовая загрузка из CSV ")
        print("5. Постраничный вывод ")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            add_or_update_user()
        elif choice == '2':
            search_by_pattern()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            bulk_insert_from_csv()
        elif choice == '5':
            get_paginated()
        elif choice == '0':
            break
        else:
            print("Неверный выбор")

    cur.close()
    conn.close()

if __name__ == "__main__":
    menu()