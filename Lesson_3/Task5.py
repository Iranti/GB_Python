'''Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''


my_input = input('Введите несколько чисел через пробел: \n')
my_list = my_input.split(' ')

def sum_list():
    sum_list = 0
    for i in my_list:
        if i.isdigit():
            i = int(i)
            sum_list += i
            return sum_list
        else:
            break
            return sum_list

print(sum_list())

my_new_input = input('Введите еще несколько чисел через пробел: \n')
my_new_list = my_new_input.split(' ')

def sum_new_list():
    sum_new_list = sum_list
    for i in my_new_list:
        if i.isdigit():
            i = int(i)
            sum_new_list += i
            return sum_list
        else:
            return sum_new_list
            break

print(sum_new_list())