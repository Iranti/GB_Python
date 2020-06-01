#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# . Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def direction(self, to):
        direct = ['влево', 'вправо']
        if to == direct[0]:
            print('Машина повернула влево')
        if to == direct[1]:
            print('Машина повернула вправо')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

a = Car(30,'black', 'Lexus', False)
print(a)
print(a.name)
a.go()
a.direction('влево')
a.show_speed()


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            speed_l = self.speed - 60
            print(f'Превышение скорости на: {speed_l}')
        else: print(f'Текущая скорость: {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            speed_l = self.speed - 40
            print(f'Превышение скорости на: {speed_l}')
        else: print(f'Текущая скорость: {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

car_a = TownCar(70, 'red', 'Volvo', False)
print(car_a.name)
print(car_a.show_speed())

car_b = SportCar(110, 'yellow', 'Ferrari', True)
print(car_b.name)
print(car_b.show_speed())

car_c = WorkCar(80, 'white', 'Gazell', False)
print(car_c.name)
print(car_c.show_speed())

car_d = PoliceCar(60, 'blue', 'Ford', True)
print(car_d.name)
print(car_d.show_speed())