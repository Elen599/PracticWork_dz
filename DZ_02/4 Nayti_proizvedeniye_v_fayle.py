# Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import*

number = int(input("Введите число: "))

listInt = []

for i in range(number):
    listInt.append(randint(-number, number))
print(listInt)

with open("list_4.txt", "r") as file:
    result = file.read().split('\n')
file.close()
print(result)
print(f'Произведение {int(result[0])} и {int(result[1])}', f'элементов сгенерированного массива = {listInt[int(result[0])] * listInt[int(result[1])]}') 