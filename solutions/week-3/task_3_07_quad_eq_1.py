'''
Квадратное уравнение - 1

Даны действительные коэффициенты a, b, c, при этом a != 0.

Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.

Формат ввода: Вводятся три действительных числа.
Формат вывода: Если уравнение имеет два корня, выведите два корня
в порядке возрастания, если один корень — выведите одно число,
если нет корней — не выводите ничего.
'''

a, b, c = float(input()), float(input()), float(input())

d = b ** 2 - 4 * a * c

if d == 0:
    x = -b/(2 * a)
    print(x)
elif d > 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(x1, x2)