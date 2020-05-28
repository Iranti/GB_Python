#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text5.txt', 'w') as calculator:
    my_list = ['3', '6', '8', '14', '34', '123\n']
    my_list_str = ' '.join(my_list)
    calculator.write(my_list_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])

    sum_input = sum(my_list)
    sum_input_str = str(sum_input)
    calculator.write(sum_input_str)






