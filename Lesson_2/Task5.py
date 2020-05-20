# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].



new_rank = input('Введите новый рейтинг\n')

while True:
    if new_rank.isdigit():
        new_rank = int(new_rank)
    else: print('Неверный формат числа')
    break


my_list = [7, 5, 3, 3, 2]

i = 0
for el in my_list:
    if new_rank >= my_list[i]:
        my_new_list = my_list.insert(i, new_rank)
        print(my_new_list)
        break
    elif my_list[-1] > new_rank:
        my_new_list = my_list.append(new_rank)
        print(my_new_list)
    elif new_rank < my_list[i]:
        i += 1


print(my_list)
