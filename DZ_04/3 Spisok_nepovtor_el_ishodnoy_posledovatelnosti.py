# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
# (удобно решать через словари) 
# Пример: 47756688399943 -> [5]
#         1113384455229 -> [8,9]
#         1115566773322 -> []
from random import randint as rnd

uniqueNum = {}
finalList = ''
oneList = ''

for i in range(20):
    oneList += str(rnd(0,9))
print(f"Задана последовательность цифр: {oneList}")

for el in oneList:
    if uniqueNum.get(el):
        uniqueNum[el] = uniqueNum.get(el) + 1
    else:
        uniqueNum[el] = 1
for i in uniqueNum.items():
    if i[1] == 1:
        finalList += str(i[0])
        
if finalList: 
    print(f"Уникальные цифры {finalList}")
else:
    print("Повторяющихся цифр нет")