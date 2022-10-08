# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from HW4 import createEquation

# Функция заполнения словаря элементами, удаляя из уравнения знаки и x^
def dictEquation():
    equation = createEquation()
    dictionary = {}

    equation = equation.replace(" + ", " +").replace(" - ", " -").split()[:-2]

    for i in range(len(equation)):
        equation[i] = equation[i].replace("+", "").split("x^")
        dictionary[int(equation[i][1])] = int(equation[i][0])

    return dictionary

finalWork = {}
work1 = dictEquation()
work2 = dictEquation()


# сложение 2х словарей
for i in range(max(len(work1), len(work2)), -1, -1):
    first = work1.get(i)
    second = work2.get(i)
    if first != None or second != None:
        finalWork[i] = (first if first != None else 0) + (second if second != None else 0)

# Функция сборки уравнения
def assemblyEquation(finalWork: dict):
    finalEq = ''
    first = True
    for d in finalWork.items():
        if first:
            first = False
            if d[1] > 0:
                finalEq += str(d[1]) + 'x^' + str(d[0])
            if d[1] < 0:
                finalEq += '-' + str(abs(d[1])) + 'x^' + str(d[0])
        else:
            if d[1] > 0:
                finalEq += ' + ' + str(d[1]) + 'x^' + str(d[0])
            if d[1] < 0:
                finalEq += ' - ' + str(abs(d[1])) + 'x^' + str(d[0])          
    return finalEq + ' = 0'

work1 = assemblyEquation(work1)
work2 = assemblyEquation(work2)

finalWork = assemblyEquation(finalWork)

with open('equation_one5.txt', 'w') as data: 
    data.write(work1)
with open('equation_two5.txt', 'w') as data: 
    data.write(work2)
with open('sumEquation5.txt', 'w') as data: 
    data.write(finalWork)