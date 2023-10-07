import os, re

def phone_number(n):  # изменение телефонного номера
    n = n.removeprefix("+")
    n = re.sub("()-", " ", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def printData(data):  # Функция вывода телефонной книги 
    phoneBook = []
    splitLine = "=" * 49
    print(splitLine)
    print(" №  Фамилия        Имя          Номер телефона")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "Фамилия": lastName,
                "Имя": name,
                "Номер телефона": phone_number(phone),
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15}")

    print(splitLine)


def showContacts(fileName):  #  открытие телефонной книги
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n нажмите любую кнопку ")


def addContact(fileName):  # добавление нового контакта в телефонную книгу
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите фамилию: ") + ","
        res += input("Введите имя: ") + ","
        res += input("Введите номер телефона: ")

        file.write(res + "\n")

    input("\nКонтакт создан\n нажмите любую кнопку ")


def findContact(fileName):  # Функция поиска контактов в телефонной книге
    os.system("cls")
    find = input("Введите данные для поиска контакта: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for name in data:
            if find in name:
                result.append(name)
                # break

    if len(result) != 0:
        printData(result)
    else:
        print(f"Контакт'{find}' не найден.")

    input("\n нажмите любую кнопку ")


def changeContact(fileName):  # Изменение контакта
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите ноимер контакта чтобы изменить или 0 чтобы вернуться в главное меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите имененную фамилию: ")
            newName = input("Введите измененное имя: ")
            newPhone = input("Введите новый телефон: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт изменен")
                input("\n нажмите любую кнопку ")
        else:
            return


def deleteContact(fileName):  # Удаление контакта
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта чтобы удалить или 0 для выхода в главное меню: ")
        )
        if numberContact != 0:
            print(f"Удаленная запись: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input(" нажмите любую кнопку ")


def MainList():  #  Интерфейс главного меню
    print("#####   Телефонная книга   #####")
    print("=" * 26)
    print(" 1 - Показать контакты")
    print(" 2 - Добавить контакт")
    print(" 3 - Найти контакт")
    print(" 4 - изменить контакт")
    print(" 5 - Удалить контакт")
    print("\n 0 - Выход")
    print("=" * 26)


def main(file_name):  # Главное меню
    while True:
        os.system("cls")
        MainList()
        userChoice = int(input("Введите от 1 до 5 или 0 чтобы выйти: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("Спасибо")
            return


path = ""

main(path)