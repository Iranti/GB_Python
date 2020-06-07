#Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    #real = 0
    #imag = 0

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        self.digit = complex(self.real, self.imag)

    def __add__(self, other = complex):
        #return complex((self.real + other.real), (self.imag + other.imag))
        return self.digit + other

    def __mul__(self, other = complex):
        return self.digit * other
        #return complex(((self.real * other.real) - (self.other * self.imag)), ((self.real * other.imag) + (self.imag * other.real)))



c = Complex(3, 4)
d = Complex(4, 5)
print(c.digit)
print(d.digit)
print(c.__add__(5+6j))
print(c.__mul__(5+6j))
print(c.digit + d.digit)
print(c.digit * d.digit)