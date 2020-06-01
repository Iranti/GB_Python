#Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

salary = {"wage": 20000, "bonus": 10000}


class Worker():
    name = input()
    surname = input()
    __income = salary["wage"]
    position = 'Программист'


class Position(Worker):

    def get_full_name(self):
        name = Worker.name
        surname = Worker.surname
        full_name = print(f'{name} {surname}')


    def total_income(self):
        income = Worker._Worker__income
        bonus = salary["bonus"]
        total_income = income + bonus
        print(total_income)

worker_a = Worker()
print(worker_a.position)
position_worker_a = Position()
position_worker_a.get_full_name()
position_worker_a.total_income()
print(worker_a._Worker__income)



