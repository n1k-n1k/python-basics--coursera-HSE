'''
Больше предыдущего

Дан список чисел.
Выведите все элементы списка, которые больше предыдущего элемента.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
'''

num_list = list(map(int, input().split()))

prev = num_list[0]
result = []
for i in range(1, len(num_list)):
    if num_list[i] > prev:
        result.append(num_list[i])
    prev = num_list[i]

print(*result)
