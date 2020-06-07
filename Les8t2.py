#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDevisionError(Exception):

    @staticmethod
    def division(x, y):
        try:
            res = x / y
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        else:
            print(res)
        finally:
            print('Вы можете продолжить работать с программой')


ZeroDevisionError.division(2,0)

