'''
Добавить, умножить

Добавьте в предыдущий класс следующие методы:
__add__, принимающий вторую матрицу того же размера
и возвращающий сумму матриц.

__mul__, принимающий число типа int или float
и возвращающий матрицу, умноженную на скаляр.

__rmul__, делающий то же самое, что и __mul__.
Этот метод будет вызван в том случае, аргумент находится справа.
Для реализации этого метода в коде класса достаточно написать
__rmul__ = __mul__.
'''

from copy import deepcopy
from sys import stdin


class Matrix:
    def __init__(self, lst):
        self.m = deepcopy(lst)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, s)) for s in self.m])

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        return Matrix([[self.m[i][j] + other.m[i][j]
                        for j in range(len(self.m[0]))]
                       for i in range(len(self.m))])

    def __mul__(self, other):
        return Matrix([[self.m[i][j] * other
                        for j in range(len(self.m[0]))]
                       for i in range(len(self.m))])

    __rmul__ = __mul__


exec(stdin.read())
