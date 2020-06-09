# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа.
import math

class Cell:

    def __init__(self, unit):
        self.unit = int(unit)

    def __add__(self, other):
        return self.unit + other

    def __sub__(self, other):
        if self.unit != other:
            return math.fabs(int(self.unit) - int(other))

    def __mul__(self, other):
        return self.unit * other

    def __truediv__(self, other):
        return round(self.unit / other)

    def make_order(self, number):
        self.number = number
        for i in range(1, self.unit):
            if i % self.number == 0:
                print(i, end='\n')
            else: print(i, end=' ')


cell_a = Cell(18)
cell_b = Cell(10)
cell_c = Cell(5)
print(cell_a.__add__(10))
print(cell_b.__sub__(13))
print(cell_a.__truediv__(3))
print(cell_c.__mul__(5))
cell_a.make_order(3)

