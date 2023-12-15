

finish = True

while finish == True:

    print("===Контакты===")
    print("==============")
    print('1. Просмотр всех контактов')
    print('2. Поиск')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Выход')
    print("==============")

    userInput = int(input('Выбор:'))
    file = 'phoneBook.txt'
   
    if userInput == 1:      ### Просмотр данных из файла
        print("==============")
        with open(file, 'r') as data:
            for line in data:
                print(line)
        print("==============")
        
    elif userInput == 2:    ### Поиск по файлу по совпаднию введенной строки , так и не смог додумать или найти в гугле красивый вывод в консаль при записи данных таким способом
        print("==============")
        findInput = input("Введите имя:")
        lowInput = findInput.lower()
        print("==============")
        with open(file) as file:
            lines = file.readlines()
            
            for line in lines:
                if lowInput in line:
                    print(line)
                    
    elif userInput == 3:    ### Добавление контакта
        print("==============")
        name = input('Введите имя: ')
        lowerName = name.lower()
        number = input('Введите номер: ')
        email = input('Введите почту: ')
        print("==============")
        newContact = {lowerName : {'Номер' : number,'Почта' :email}}
        
        with open(file, 'a') as file:
            for key, val in newContact.items():
                file.write('{} {}\n'.format(key,val))
       
       
    elif userInput == 4:    ### Изменение контакта / Удаление
         finish = False

            
    elif userInput == 5:
        finish = False 
            
    
        
        







