# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input("Введите вещественное число: ")
count = len(num)
num = float(num)
sum = 0

for i in range(count):
    num *= 10

while int(num) != 0:
    sum += num%10
    num //= 10
print(f"Сумма цифр в числе равна {int(sum)}")    