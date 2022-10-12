# --coding: utf-8 --
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

# Функция сжатия (кодирование) данных 
def coding(data):
    package = ''
    prev_char = ''
    count = 0
    for char in data:
        if char != prev_char:
            if prev_char:
                package += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        package += str(count) + prev_char
        return package


# Функция раскодирования данных
def recovery(data):
    unpacking = ''
    char_count = ''
    for char in data:
        if char.isdigit():
            char_count += char
        else:
            unpacking += char * int(char_count)
            char_count = ''
    return unpacking

# Код программы:
code = input("Задайте порядок букв, например: aaaannyyyyyy: "'\n')

with open('package4_1.txt', 'w', encoding = 'utf-8') as data:
    data.write(code)

package = coding(code)
print(f'Сжатые данные из файла compression4_1: {code} ==> {package}')

with open('unpacking4_2.txt', 'w', encoding = 'utf-8') as data:
    data.write(package)

unpacking = recovery(package)
print(f'Восстановленные данные из файла unpacking4_2.txt: {package} ==> {unpacking}')

with open('package4_1.txt', 'w', encoding = 'utf-8') as data:
    data.write(unpacking)