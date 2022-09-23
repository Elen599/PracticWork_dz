# ¬(X V Y V Z) = ¬X ^ ¬Y ^ ¬Z

Uravnenie_1 = lambda x, y, z: not (x and y and z)
Uravnenie_2 = lambda x, y, z: (not x) or (not y) or (not z)

# Код программы
print("Проверим истинность выражения\n¬(X V Y V Z) = ¬X ^ ¬Y ^ ¬Z\nПодставим вместо x, y, z единицы и нули всевозможными вариациями")
x, y, z = 1, 1, 1
if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
x, y, z = 1, 1, 0
if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
x, y, z = 1, 0, 1
if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
x, y, z = 1, 0, 0
if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
x, y, z = 0, 1, 1
if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
x, y, z = 0, 1, 0
if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
x, y, z = 0, 0, 1
if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
x, y, z = 0, 0, 0
if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
