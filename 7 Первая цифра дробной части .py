# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
n = float (input("Введите число: "))
if n%1 == 0:
    print("Числа дробной части нет.")
else:
    n *= 10
    n = int(n)
    n = n%10
    print(f"Первая цифра дробной части будет: {n}") 