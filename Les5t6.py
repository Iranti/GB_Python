#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('text6.txt', 'r') as curriculum:
    content = curriculum.read()
    #print(content)
    #print(type(content))

    cont_list_lines = content.split('\n')
    #print(cont_list_lines)
    #print(type(cont_list_lines))
    for line in cont_list_lines:
        cont_list_line = line.split(':')
        print(cont_list_line)

        value_line = cont_list_line[1]

        value_line_list = value_line.split(' ')
        value_line_list = [str.rstrip(' ') for str in value_line_list]
        print(value_line_list)

    my_dict = {}

    for key, val in my_dict.items():
        for line in cont_list_line:
            key = cont_list_line[0]
            val = value_line_list
            my_dict[key] = val

    print(my_dict)


