#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
#а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
#(со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]


with open('text7.txt') as source:
    revenue_true = 0
    revenue_firm = 0
    firm_dict = {}
    av_rev_dict = {}

    for line in source:
        line_list = line.split(' ')
        line_list = [str.rstrip() for str in line_list]
        #print(line_list)
        revenue = float(int(line_list[2]) - int(line_list[3]))
        print(f'Прибыль: {revenue}')
        if revenue > 0:
            revenue_true += revenue
            revenue_firm += 1
        print(revenue_true)
        firm_dict[line_list[0]] = revenue

    print(firm_dict)

    revenue_av = revenue_true / revenue_firm
    print(revenue_av)

    av_rev_dict = {'average profit': revenue_av}

    total_dict = [av_rev_dict, firm_dict]

    print(total_dict)

import json

with open("my_file_7.json", "w") as write_f:
    json.dump(total_dict, write_f)



