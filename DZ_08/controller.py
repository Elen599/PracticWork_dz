import model
import view

def start():
    open_file()
    view.print_phone_book()
    view.main_menu()


def open_file():
    with open(model.path, 'r', encoding="UTF-8") as data:
        contact_list = data.read().split("\n")
        model.phonebook = contact_list


def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    contact = f'{name} {surname} {phone}\n'
    model.phonebook.append(contact)
    view.print_phone_book()


def remove_contact():
    num = int(input('Выберите номер элемента для удаления:'))
    model.phonebook.pop(num)
    view.print_phone_book()


def change_contact():
    choice1 = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменить(0-имя, 1-фамилия, 2-номер): '))

    contact = model.phonebook.pop(choice1).split(' ')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    model.phonebook.insert(choice1, ' '.join(contact))
    view.print_phone_book()


def find_contact():
    choice = input('Введите искомый элемент (имя или фамилию): ')
    print()
    for i, el in enumerate(model.phonebook):
        if choice.lower() in el.lower():
            print(model.phonebook[i])


def save_contact():
    with open(model.path, 'w', encoding="UTF-8") as data:
        data.write('\n'.join(model.phonebook))