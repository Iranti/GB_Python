# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

var_inp = input('Введите несколько слов\n')
print(var_inp)
var_inp = var_inp.title()
var_str = var_inp.split(' ')
print(var_str)
n = 0
for i in var_str:
    n += 1
    print(n, ':', i[:9])
