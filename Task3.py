# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

var_season = ('зима', 'весна', 'лето', 'осень' )

var_year = {
'зима': (1, 2, 12),
'весна': (3, 4, 5),
'лето': (6, 7, 8),
'осень': (9, 10, 11),
}

var_month = input('Введите месяц в виде целого числа от 1 до 12\n')

while True:
    if var_month.isdigit():
        var_month = int(var_month)
        break
    else: print('Введите верную форму числа')
    break

for key, value in var_year.items():
    if var_month in value:
        print(key)
        break

