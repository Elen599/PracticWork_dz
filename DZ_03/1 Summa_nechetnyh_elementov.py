# Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import*

number = int(input("Введите число элементов: "))

listInt = []
for i in range(number):
    listInt.append(randint(0,10))
print(listInt)

sum = 0
for i in range(len(listInt)):
    if i%2 == 1:
        sum += listInt[i] 
print(f"Сумма элементов списка на нечетных позициях равна: {sum} ")    