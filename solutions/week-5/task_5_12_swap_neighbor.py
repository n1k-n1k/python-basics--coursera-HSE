'''
Переставить соседние

Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
Если элементов нечетное число, то последний элемент остается на своем месте.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
'''

num_list = list(map(int, input().split()))

for i in range(0, len(num_list) - 1, 2):
    num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]

print(*num_list)
