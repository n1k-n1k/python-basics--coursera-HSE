'''
Переставить min и max

В списке все элементы попарно различны.
Поменяйте местами минимальный и максимальный элемент этого списка.

Формат ввода
Вводится список целых чисел. Все числа списка находятся на одной строке.
'''

num_list = list(map(int, input().split()))
min_ind = num_list.index(min(num_list))
max_ind = num_list.index(max(num_list))

num_list[min_ind], num_list[max_ind] = num_list[max_ind], num_list[min_ind]
print(*num_list)
