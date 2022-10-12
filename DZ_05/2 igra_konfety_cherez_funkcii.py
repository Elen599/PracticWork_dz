# --coding: utf-8 --
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from os import system
from random import randrange

def do_plaer(balance, plaer):
    if plaer:
        num = 'ПЕРВЫЙ'
    else:
        num = 'ВТОРОЙ'
    box = int(input(f"Берет конфеты {num} игрок (от 1 до 10):  "))
    system('cls')
    if 0 < box < 11 :
        balance -= box
        if balance > 0:
            print(f"Конфет осталось {balance}")
        else:
            print(f"Все конфеты разобраны\nПобедил игрок {num}")
        plaer = not plaer
    else:
        print("Такое количество конфет брать нельзя!")
    return balance, plaer

def bot_do(balance, box, plaer):
    print(f"Конфеты берет компьютер: {box}")
    balance -= box
    if balance > 0:
        print(f"Конфет осталось {balance}")
    else:
        print("Все конфеты разобраны\nПобедил компьютер")
    plaer = not plaer
    return balance, plaer

print('\n\"На столе лежит 150 конфет.\nИграют два игрока, делая ход друг после друга.\nЗа один ход можно забрать от 1 до 28 конфет.\nВыигрывает тот, кто возьмет конфеты последним.\"\n')

print("Режимы игры:\n1-два игрока\n2-игра с простым ботом\n3-игра с умным ботом\n")
change = int (input("Выберите режим игры:  "))

balance = 100
plaer = randrange(0, 2)

if change == 1:
    while balance > 0:
        if plaer:
            balance, plaer = do_plaer(balance, plaer)
        else:
            balance, plaer = do_plaer(balance, plaer)
elif change == 2:
    while balance > 0:
        if plaer:
            balance, plaer = do_plaer(balance, plaer)
        else:
            box = randrange(1, 11)
            balance, plaer = bot_do(balance, box, plaer)   
elif change == 3:
    while balance > 0:
        if plaer:
            balance, plaer = do_plaer(balance, plaer)
        else:
            box = balance % 11
            if box == 0:
                box = randrange(1, 11)
            balance, plaer = bot_do(balance, box, plaer)
else:
    print("Ошибка выбора режима")