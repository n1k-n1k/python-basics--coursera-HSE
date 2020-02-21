'''
Сложение без сложения

Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
целых неотрицательных чисел. Из всех арифметических операций допускаются
только +1 и -1. Также нельзя использовать циклы.

Формат ввода
Вводятся два удовлетворяющих условию задачи числа. Числа не превышают 900.
'''


def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if 0 < a <= b:
        return sum(a - 1, b + 1)
    if 0 < b < a:
        return sum(a + 1, b - 1)


a, b = int(input()), int(input())
print(sum(a, b))
