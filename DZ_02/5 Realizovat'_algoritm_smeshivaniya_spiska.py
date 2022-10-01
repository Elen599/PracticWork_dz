# Реализуйте алгоритм перемешивания списка.
from random import*

num = int(input("Введите число: "))
list_origin = []
result = []

for i in range(num):
    list_origin.append(i)
print(f"Оригинальный список:\n {list_origin}\n")

for i in range(num):
    index = randrange (0,len(list_origin))
    result.append(list_origin[index])
    list_origin.pop(index)
print(f"Перемешанный список: \n {result}")     