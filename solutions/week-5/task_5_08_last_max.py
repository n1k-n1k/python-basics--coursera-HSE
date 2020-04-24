'''
Последний максимум

Найдите наибольшее значение в списке и индекс последнего элемента,
который имеет данное значение за один проход по списку,
не модифицируя этот список и не используя дополнительного списка.

Выведите два значения.
'''

num_list = list(map(int, input().split()))

max_val = num_list[0]
max_ind = 0

for i, n in enumerate(num_list):
    if n >= max_val:
        max_val = n
        max_ind = i

print(max_val, max_ind)
