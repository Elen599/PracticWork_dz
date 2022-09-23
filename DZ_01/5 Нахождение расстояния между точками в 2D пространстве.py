from math import*

# Подсчет длины метода
def lenght_vector(x1, x2, y1, y2):
    x = x2-x1
    y = y2-y1
    s = sqrt(x**2 + y**2)
    return s    

# Код программы
x1 = int (input("Введите координату точки x1: "))
y1 = int (input("Введите координату точки y1: "))
x2 = int (input("Введите координату точки x2: "))
y2 = int (input("Введите координату точки y2: "))
print(lenght_vector(x1, x2, y1, y2))