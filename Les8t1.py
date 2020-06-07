# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с
# декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self, data_input = str):
        self.data_input = data_input

    @classmethod
    def digit(cls, data_input):
        data_list = data_input.split('-')
        data_list_int = []
        for i in range(len(data_list)):
            try:
                data_list[i] = int(data_list[i])
                data_list_int.append(data_list[i])
            except ValueError:
                print('Неверная запись данных')
        return data_list_int

    #@staticmethod - ## 2ой вариант решения
    #def valid(data_input):
        #data_list = data_input.split('-')
        #if data_list[0].isdigit() and data_list[1].isdigit() and data_list[2].isdigit():
            #if int(data_list[2]) <= 99:
                #if int(data_list[1]) <=12:
                    #if int(data_list[0]) <=28:
                        #print('Дата введена в верном формате')
                    #elif 29 <= int(data_list[0]) <31 and int(data_list[1]) in [4, 6, 9, 11]:
                        #print('Дата введена в верном формате')
                    #elif int(data_list[0]) == 31 and int(data_list[1]) in [1, 3, 5, 7, 8, 10, 12]:
                        #print('Дата введена в верном формате')
                    #elif 29 <= int(data_list[0]) < 31 and int(data_list[1]) in [4, 6, 9, 11]:
                        #print('Дата введена в верном формате')
                    #else: print('Неверно указан день')
                #else: print('Неверно указан месяц')
            #else: print('Неверно указан год')
        #else: print('Неверно указана дата')
        #return f'Функция обработана'

    @staticmethod
    def valid(data_input):
        data_list_int = Data.digit(data_input)
        try:
            if data_list_int[2] <= 99:
                if data_list_int[1] <= 12:
                    if data_list_int[0] <= 28:
                        print('Дата введена в верном формате')
                    elif 29 <= data_list_int[0] < 31 and data_list_int[1] in [4, 6, 9, 11]:
                        print('Дата введена в верном формате')
                    elif data_list_int[0] == 31 and data_list_int[1] in [1, 3, 5, 7, 8, 10, 12]:
                        print('Дата введена в верном формате')
                    elif 29 <= data_list_int[0] < 31 and data_list_int[1] in [4, 6, 9, 11]:
                        print('Дата введена в верном формате')
                    else:
                        print('Неверно указан день')
                else:
                    print('Неверно указан месяц')
            else:
                print('Неверно указан год')
        except IndexError:
            print('Не введено три числа в требуемом формате')
        return f'Функция обработана'

mc = Data()
print(mc.digit('12-03-56'))
print(mc.digit('rgerg'))
print(Data.valid('13-03-54'))
print(Data.valid('32-03-54'))
print(Data.valid('32-13-102'))
print(Data.valid('дрмгг'))

