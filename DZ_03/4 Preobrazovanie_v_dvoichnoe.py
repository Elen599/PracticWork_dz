# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal_n = int(input("Введите десятичное число: "))

binary_n = ''
while decimal_n > 0:
    binary_n = str(decimal_n % 2) + binary_n
    decimal_n //= 2 
print(f"Число {decimal_n} преобразовано в двоичное => {binary_n}")