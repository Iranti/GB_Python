''' Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
 начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func().'''

text = input('Type a word in lower case\n')

def int_func():
    return text.title()

print(int_func())

text = input('Type several words in lower case with spaces inbetween\n')
text_list = text.split(' ')
print(int_func())