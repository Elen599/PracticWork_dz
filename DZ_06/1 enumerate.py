# --coding: utf-8 --
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open('abv1.txt', 'r', encoding = 'utf-8') as data:
#     text = data.read().split(' ')
# print(text)
# for i in text:
#    if "абв" in i:
#        text.remove(i)

# with open('final_abv1.txt', 'w', encoding = 'utf-8') as data: 
#     for i in text:
#         data.write(i + ' ')

#### enumerate #############################################################

def error_remove(text):
    new_text = ''
    for i, el in enumerate(text):
        if "абв" in el:
            text.pop(i)
    for el in text:
        new_text += el + ' '
    return new_text

with open('abv1.txt', 'r', encoding = 'utf-8') as data:
    text = data.read().split(' ')

new_text = error_remove(text)
with open('final_abv1.txt', 'w', encoding = 'utf-8') as data: 
    data.write(new_text)