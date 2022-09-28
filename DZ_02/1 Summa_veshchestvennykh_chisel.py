# --coding: utf-8 --
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = float(input("Введите число: "))
num = str(num)
num = num.replace('.', '')
n = len(num)
num = int(num)
sum = 0

for i in range(n):
    sum += num%10
    num = num//10
print(f"Сумма цифр в числе равна {sum}")    