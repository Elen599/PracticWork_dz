# Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

array = [1, 2, 3, 5, 7]

with open("list_4.txt", "r") as file:
    num = file.readlines()
file.close()

result = []
for i in range(len(array)):
    result.append(array[i] * int(num[i]))
print(f'Список элементов, хранящихся в файле ".txt":\n{num}\nЗаданый список элементов:\n{array}\nПроизведения элементов в списках:\n{result}') 