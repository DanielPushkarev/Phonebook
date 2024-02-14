# Создаем пустой словарь для хранения записей в справочнике
phonebook = {}


# Функция для вывода записей постранично
def display_entries(entries):
    # Определяем количество записей на одной странице
    page_size = 5
    # Разбиваем список записей на страницы
    pages = [entries[i:i + page_size] for i in range(0, len(entries), page_size)]

    # Выводим каждую страницу
    for page in pages:
        print("Страница:")
        for entry in page:
            print(entry)
        print()


# Функция для добавления новой записи в справочник
def add_entry():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    lastname = input("Введите отчество: ")
    number_1 = input("Введите номер личного телефона: ")
    number_2 = input("Введите номер рабочего телефона: ")
    work = input("Введите место работы: ")
    phonebook[surname, name, lastname, work] = number_1, number_2
    print("Запись добавлена!")


# Функция для редактирования записей в справочнике
def edit_entry():
    name = input("Введите имя записи, которую хотите отредактировать: ")

    # Проверяем, существует ли запись с указанным именем
    if name in phonebook:
        new_number = input("Введите новый номер телефона: ")
        phonebook[name] = new_number
        print("Запись отредактирована!")
    else:
        print("Запись не найдена!")


# Функция для поиска записей по характеристикам
def search_entries():
    search_term = input("Введите характеристику для поиска: ")

    # Ищем записи, содержащие введенную характеристику
    search_results = [entry for entry in phonebook.items() if search_term in entry[0] or search_term in entry[1]]

    if search_results:
        print("Результаты поиска:")
        for entry in search_results:
            print(entry)
    else:
        print("Записи не найдены!")


# Основной цикл программы
while True:
    print("Телефонный справочник")
    print("1. Вывести записи на экран")
    print("2. Добавить новую запись")
    print("3. Редактировать запись")
    print("4. Поиск записей")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        display_entries(phonebook.items())
    elif choice == "2":
        add_entry()
    elif choice == "3":
        edit_entry()
    elif choice == "4":
        search_entries()
    elif choice == "5":
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")

# Открываем файл для записи
with open('text.txt', 'w') as file:
    # Выводим информацию в файл
    file.write(str(phonebook))

# Завершение работы с файлом
file.close()
