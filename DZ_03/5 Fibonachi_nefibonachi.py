# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("Введите номер элемента ряда фибоначчи: "))

fib = [0, 1]
for i in range(2, num+1):
    fib.append (fib[i-1] + fib[i-2])
fib2 = []
for i in range(1, num+1):
    fib2.append(fib[i])

for i in range(len(fib2)):
    if i%2 == 1:
        fib2[i] = -fib2[i]
fib2.reverse()
result = fib2 + fib

print(result)