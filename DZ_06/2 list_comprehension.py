# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# from random import*

# num = randrange(5, 10)
# list_f = []
# for i in range(num):
#     list_f.append(random()*10)
# print(list_f)

# fract = []
# for i in list_f:
#     fract.append(i - int(i))
   
# print(f"Разницa между максимальной и минимальной дробной частью равна {max(fract) - min(fract)}")

####### list Comprehension ####################################################################

from random import*

num = randrange(5, 10)
list_num = (list(random()*10 for i in range(num))) 
print(list_num)   

fract = []
for i in list_num:
    fract.append(i - int(i))
   
print(f"Разницa между максимальной и минимальной дробной частью равна {max(fract) - min(fract)}")