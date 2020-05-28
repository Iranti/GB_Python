#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('ínput.txt', 'w') as file_input:
    content = input('Введите данные: ')
    content_list = content.split(' ')
    file_input.writelines(content_list[0])
   # for i in range(len(content_list)):
       # if content_list[i] == [']:
    file_input.close()


