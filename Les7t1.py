from copy import deepcopy

class Matrix:

    def __init__(self, data:list):
        self.data = deepcopy(data)
        self._length = (len(max(self.data, key=len)), len(self.data))
        if len(min(self.data, key=len)) != self.length[0]:
            self.new_length()

    @property
    def length(self):
        return self._length

    def new_length(self):
        for itm in self.data:
            tmp = self._length[0] - len(itm)
            if tmp:
                itm.extend(0 for _ in range(tmp))

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        return self.data.__iter__()

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'Это не матрица, это  {type(other).__name__}')
        if self._length != other._length:
            raise ValueError(f'Размер матриц не совпадает: {self._length} and {other._length}')
        return Matrix(list(map(lambda y: list(map(sum, y)),
                               map(lambda x: list(zip(*x)), zip(self, other)))))

    def __str__(self):
        max_len_itm = len(str(max(map(lambda item: max(item, key=lambda x: len(str(x))), self.data))))
        if not max_len_itm & 1:
            max_len_itm += 1
        result = ''
        for line in self.data:
            result += ''.join([f'{itm:>{max_len_itm}}' for itm in line]) + '\n'
        return result


matrix_a = Matrix([[1,2,4],[6,9,12],[6,15,18]])
print(matrix_a)
matrix_b = Matrix([[3456, 2432341, 3242], [345351, 232342, 4582], [422, -2342, -333]])
print(matrix_b)
print(matrix_a.__add__(matrix_b))
#print(matrix_a)

