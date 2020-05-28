#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from functools import reduce

with open('text3.txt', 'r') as office:
    content_dict = {}
    for str_line in office:
        str_list = str_line.split(' ')
        str_list = [str.rstrip() for str in str_list]
        content_dict[str_list[0]] = str_list[1]

    print(content_dict)

    for key, value in content_dict.items():
        value = int(value)
        if value < 20000:
            print(f'Сотрудник, который имеет оклад менее 20000 р.: {key}')


    for key, value in content_dict.items():
        content_dict[key] = int(value)


    def mult(x, y):
        return (x + y)/2

    my_mult = reduce(mult, content_dict.values())

    print(f'Средний оклад сотрудников {my_mult}')
