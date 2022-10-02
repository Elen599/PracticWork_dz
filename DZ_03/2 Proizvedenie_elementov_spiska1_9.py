# Напишите программу, которая найдёт произведение пар чисел списка (Cписок создаем рандомно). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
#         [2, 3, 5, 6] => [12, 15]
from random import*

num = int(input("Введите число: "))

listInt = []
for i in range(num):
    listInt.append(randint(0, 10))

if num %2 == 0:
    midle = num//2
else: 
    midle = num //2 + 1 

mult = []
for i in range(midle):
    mult.append(listInt[i]*listInt[-i-1])
       
print(f"Произведения пар чисел списка {listInt} => {mult}")