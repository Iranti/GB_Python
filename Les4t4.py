#4. Реализовать формирование списка, используя функцию range() и
# возможности генератора. В список должны войти четные числа от 100 до 1000
# (включая границы). Необходимо получить результат вычисления произведения всех
# элементов списка. Подсказка: использовать функцию reduce().

from functools import reduce

my_list = list(range(99,1001))

my_new_list = [ el for el in my_list if el % 2 == 0]

def mult (x, y):
    return x * y

my_mult = reduce(mult , my_list)

print(my_mult)


