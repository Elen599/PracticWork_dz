# --coding: utf-8 --                                         # x o o  
# Создайте программу для игры в ""Крестики-нолики"".         # o x x 
                                                             # x x o
# Функция действий игрока
def do_step(line, step, d, count):
    line[step[0]][step[1]] = d
    print_line(line)
    count += check_win(line, 'x')
    return line, count
    
# Функция условий побед // имя массива [индекс строки][индекс столбца]
def check_win(line, d):
    w1 = line[0][0] == line[0][1] == line[0][2] == d
    w2 = line[1][0] == line[1][1] == line[1][2] == d
    w3 = line[2][0] == line[2][1] == line[2][2] == d
    w4 = line[0][0] == line[1][1] == line[2][2] == d
    w5 = line[2][0] == line[1][1] == line[0][2] == d
    w6 = line[0][0] == line[1][0] == line[2][0] == d
    w7 = line[2][1] == line[1][1] == line[2][1] == d
    w8 = line[0][2] == line[1][2] == line[2][2] == d
    if w1 or w2 or w3 or w4 or w5 or w6 or w7 or w8:
        if d == 'x':
            print("Выиграл игрок 'X'")
        else:
            print("Выиграл игрок 'O'")
        return 9
    else:
        return 0

# Функция вывода поля
def print_line(line):
    for i in line:
        print(*i)

# Код программы
line = [['*','*','*'],['*','*','*'],['*','*','*']]
trigger = True
count = 0
print_line(line)
print("Ходит игрок 'X'")
d = 'x'
while count < 9:
    step = [int(el)-1 for el in (input("Введите две координаты через пробел от 1 до 3: ")).split()]
    if 3 > step[0] > -1 and 3 > step[1] > -1: 
        if line[step[0]][step[1]] == '*':
            if trigger:
                line, count = do_step(line, step, d, count)
                trigger = not trigger
                print("Ходит игрок 'O'") 
                d = 'o' 
            else:
                line, count = do_step(line, step, d, count)
                trigger = not trigger
                print("Ходит игрок 'X'")
                d = 'x'
            count += 1
        else:
            print("Ячейка занята")   
    else:
        print("Не верные координаты!")  
    if count == 9:
        print("НИЧЬЯ")