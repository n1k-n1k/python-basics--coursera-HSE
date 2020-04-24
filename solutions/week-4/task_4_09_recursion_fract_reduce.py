'''
Сократите дробь

Даны два натуральных числа n и m.
Сократите дробь (n / m), то есть выведите два других числа p и q таких,
что (n / m) = (p / q) или дробь (p / q), если она несократимая.

Решение оформите в виде функции ReduceFraction(n, m),
получающей значения n и m и возвращающей кортеж из двух чисел: return p, q.
Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).
'''


def gcd(a, b):
    return abs(a) if b == 0 else gcd(b, a % b)


def reduce_fraction(a, b):
    gcd_ab = gcd(a, b)
    return a // gcd_ab, b // gcd_ab


n, m = int(input()), int(input())
print(*reduce_fraction(n, m))
