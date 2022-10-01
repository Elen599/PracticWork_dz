# Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.

n = int (input("Введите число: "))
array = []

for i in range(1, n+1):
    array.append((1+1/i)**i)
print(*array)

sum = 0
for i in array:
    sum += i
print(f"Сумма {n} элементов равна: {sum}")