'''
Площадь треугольника

Даны длины сторон треугольника. Вычислите площадь треугольника.
Формат ввода: Вводятся три положительных действительных числа.
'''

a, b, c = float(input()), float(input()), float(input())

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(s)
