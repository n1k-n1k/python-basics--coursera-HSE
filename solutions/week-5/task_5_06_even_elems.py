'''
Четные элементы

Выведите все четные элементы списка.

Формат ввода: Вводится список чисел.
Все числа списка находятся на одной строке.
'''

num_list = list(map(int, input().split()))
result = list(filter(lambda n: not n % 2, num_list))
print(*result)
