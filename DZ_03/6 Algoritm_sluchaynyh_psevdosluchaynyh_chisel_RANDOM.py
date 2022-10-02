# Реализуйте алгоритм задания случайных чисел без использования встроенного 
# генератора псевдослучайных чисел. БЕЗ КАКИХ ЛИБО РАНДОМОВ
from time import*

def gen_random(num):
    gen = time()
    gen %= 1
    gen = int(num*gen)
    print(gen)

diapozon = int(input("Введите диапозон от 0 до "))
gen_random(diapozon)