# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл. Во втором также необходимо
# предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

my_list = []

def generator_int():
    for el in count(3):
        if el > 20:
            break
        else:
            my_list.append(el)


generator_int()

print(my_list)


my_new_list = []

def my_list_cycle():
    c = 0
    for i in cycle(my_list):
        if c / len(my_list) == 3:
            break
        my_new_list.append(i)
        c += 1

my_list_cycle()

print(my_new_list)