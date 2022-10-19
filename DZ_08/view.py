import model
import controller

def print_phone_book():
    for i, item in enumerate(model.phonebook):
        print(i, item)


def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Добавить контакт')
        print('2. Удалить контакт')
        print('3. Изменить контакт')
        print('4. Найти контакт')
        print('5. Сохранить контакт')
        print('0. Выйти из программы')
        choice = int(input('Выберите действие:'))
        match(choice):
            case 1:
                controller.add_contact()
                print('\nКонтакт добавлен\n')
            case 2:
                controller.remove_contact()
                print('\nКонтакт удален\n')
            case 3:
                controller.change_contact()
                print('\nКонтакт изменен\n')
            case 4:
                controller.find_contact()
                print('\nКонтакт найден\n')
            case 5:
                controller.save_contact()
                print('\nКонтакт сохранен\n')
            case _:
                break