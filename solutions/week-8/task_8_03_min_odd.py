'''
Наименьший нечетный

Выведите значение наименьшего нечетного элемента списка,
гарантируется, что хотя бы один нечётный элемент в списке есть.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
'''

print(sorted(filter(lambda x: x % 2, map(int, input().split())))[0])
