'''
Сортировка подсчетом

Дан список из N (N≤2*10⁵) элементов, которые принимают
целые значения от 0 до 100 (100 включая).

Отсортируйте этот список в порядке неубывания элементов.
Выведите полученный список.

Решение оформите в виде функции CountSort(A),
которая модифицирует передаваемый ей список.

Использовать встроенные функции сортировки нельзя.
'''


def count_sort(num_list):
    cnt = [0] * 101
    result = []

    for n in num_list:
        cnt[n] += 1

    for i in range(len(cnt)):
        for j in range(cnt[i]):
            result.append(i)

    return result


num_list = list(map(int, input().split()))
print(*count_sort(num_list))
