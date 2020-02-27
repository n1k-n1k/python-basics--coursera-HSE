'''
Ошибки, транспонирование

Добавьте в программу из предыдущей задачи класс MatrixError,
содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.

В класс Matrix внесите следующие изменения:
Добавьте в метод __add__ проверку на ошибки в размере входных данных,
чтобы при попытке сложить матрицы разных размеров было выброшено
исключение MatrixError таким образом, чтобы matrix1 поле MatrixError
стало первым аргументом __add__ (просто self), а matrix2 — вторым
(второй операнд для сложения).

Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат
(данный метод модифицирует экземпляр класса Matrix)
Реализуйте статический метод transposed, принимающий Matrix и возвращающий
транспонированную матрицу.
'''

from copy import deepcopy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, lst):
        self.m = deepcopy(lst)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, s)) for s in self.m])

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        len_m = (len(self.m), len(self.m[0]))
        len_o = (len(other.m), len(other.m[0]))

        if len_m == len_o:
            return Matrix([[self.m[i][j] + other.m[i][j]
                            for j in range(len(self.m[0]))]
                           for i in range(len(self.m))])
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        return Matrix([[self.m[i][j] * other
                        for j in range(len(self.m[0]))]
                       for i in range(len(self.m))])

    def transpose(self):
        self.m = [list(i) for i in zip(*self.m)]
        return Matrix(self.m)

    @staticmethod
    def transposed(matrix):
        return Matrix([list(i) for i in zip(*matrix.m)])

    __rmul__ = __mul__


exec(stdin.read())
