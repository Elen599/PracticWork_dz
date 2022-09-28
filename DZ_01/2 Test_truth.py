# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬(X V Y V Z) = ¬X ^ ¬Y ^ ¬Z

trigger = True
for x in [True,False]:
    for y in [True, False]:
        for z in [True, False]:
            if not (x or y or z) != (not x and not y and not z):
                print("Не верно!")
                trigger = False
                break
if trigger: print("Выражение верно!")


###########################################################################

#Uravnenie_1 = lambda x, y, z: not (x and y and z)
#Uravnenie_2 = lambda x, y, z: (not x) or (not y) or (not z)

# Код программы
#print("Проверим истинность выражения\n¬(X V Y V Z) = ¬X ^ ¬Y ^ ¬Z\nПодставим вместо x, y, z единицы и нули всевозможными вариациями")
#x, y, z = 1, 1, 1
#if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
#    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
#x, y, z = 1, 1, 0
#if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
#    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
#x, y, z = 1, 0, 1
#if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
#    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
#x, y, z = 1, 0, 0
#if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
#    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
#x, y, z = 0, 1, 1
#if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
#    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
#x, y, z = 0, 1, 0
#if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
#    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
#x, y, z = 0, 0, 1
#if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
#    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")
#x, y, z = 0, 0, 0
#if Uravnenie_1 (x, y, z) == Uravnenie_2 (x, y, z):
#    print(f"При значении x = {x} y = {y} z = {z}, выражение истинно")