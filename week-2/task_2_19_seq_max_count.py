'''
Количество элементов, равных максимуму

Последовательность состоит из натуральных чисел и завершается числом 0.
Определите количество элементов этой последовательности,
которые равны ее наибольшему элементу.

Формат ввода: Вводится последовательность целых чисел,
оканчивающаяся числом 0 (само число 0 в последовательность не входит,
а служит как признак ее окончания).
'''

n = int(input())
max_ = n
max_count = 0

while n != 0:
    if n == max_:
        max_count += 1
    elif n > max_:
        max_ = n
        max_count = 1
    n = int(input())

print(max_count)