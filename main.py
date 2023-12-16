import sys
import sqlite3  

def print_menu():  
    print ('\nВыбор пункта меню:')  
    print('1. Добавить новый контакт')  
    print('2. Просмотр контактов')  
    print('3. Изменить контакт')  
    print('4. Удаление контакта')
    print('5. Поиск контакта')
    print('0. Выход')

def addcontact():
    while True:  
        name = input("Введите имя: ") 
        if len(name) != 0:  
            break  
        else:  
            print("Пожалуйста введите имя: ")     
    while True:  
        surname = input("Введите фамилию: ")  
        if len(surname) != 0:  
            break  
        else:  
            print("Пожалуйста введите фамилию")    
    while True:  
        num = input("Введите номер(только цифры): ")  
        if not num.isdigit():  
            print("Пожалйста введите численные значения")  
            continue  
        elif len(num) != 10:  
            print("Пожалуйста введите 10 значный номер без пробелов, запятых, и прочих символов")  
            continue  
        else:  
            break  
    cursor.execute('''INSERT INTO phonebook (name, surname, phone_number) VALUES (?,?,?)''',
                                                                         (name, surname, num))  
    conn.commit()      
    print("Новый контакт " + surname + ' ' + name + " был добавлен в телефонную книгу")

def displaybook():
    cursor.execute("SELECT surname, name, phone_number FROM phonebook ORDER BY surname")
    results = cursor.fetchall()
    print(results)

def key_pair_reception(str):
    print ("\nВыберете пункт меню " + str + " (от 1 до 3)")  
    print('1. Имя')  
    print('2. Фамилия')  
    print('3. Номер телефона')  
    print('0. Вернуться в меню')
    n = int(input('Ваш выбор: '))
    if n == 1:  
        field = "name"
    elif n == 2:  
        field = "surname"
    elif n == 3:  
        field = "phone_number"
    else:
        return None
    keyword = input("\nПожалуйста введите значение: " + field )
    keypair = field + "='" + keyword + "'"
    return keypair

def editcontacts():
    s = key_pair_reception('searching')
    u = key_pair_reception('updating')
    if s != None:
        sql = "UPDATE phonebook SET " + u + " WHERE " + s
        cursor.execute(sql)
        conn.commit()
        print("Выполнено!\n")

def deletecontacts():
    s = key_pair_reception('searching')
    if s != None:
        sql = 'DELETE FROM phonebook WHERE ' + s
        cursor.execute(sql)
        conn.commit()
        print("Выполнено\n")

def findcontacts():
    s = key_pair_reception('searching')
    if s != None:
        sql = 'SELECT surname, name, phone_number FROM phonebook WHERE ' + s + ' ORDER BY surname'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

# Основная программа
print ('\nДобро пожаловать в телефонный справочник')
conn = sqlite3.connect('dataBase.db')  
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                id integer PRIMARY KEY,
                name text NOT NULL,
                surname text,
                phone_number text)''');
m = -1  
while m != 0:
    print_menu()  
    m = int(input('Ваш выбор: '))  
    if m == 1:  
        addcontact()
        continue
    elif m == 2:  
        displaybook()
        continue
    elif m == 3:  
        editcontacts()
        continue
    elif m == 4:  
        deletecontacts()
        continue
    elif m == 5:  
        findcontacts()
        continue
    elif m == 0:  
        print('Программа завершена.\n')
        conn.close()
        sys.exit(0)  
    else:  
        print('Пожалуйста следуйте инструкциям')