'''
Слияние списков

Даны два целочисленных списка A и B, упорядоченных по неубыванию.
Объедините их в один упорядоченный список С (то есть он должен содержать
len(A)+len(B) элементов). Решение оформите в виде функции merge(A, B),
возвращающей новый список. Алгоритм должен иметь сложность O(len(A)+len(B)).
Модифицировать исходные списки запрещается.
Использовать функцию sorted и метод sort запрещается.

Формат ввода
Программа получает на вход два неубывающих списка, каждый в отдельной строке.
'''


def merge(list1, list2):
    p1, p2 = 0, 0
    len1, len2 = len(list1), len(list2)
    stop = len1 + len2
    curr = None
    result = []

    while p1 + p2 < stop:
        if p1 == len1:
            result.extend(list2[p2:])
            return result

        if p2 == len2:
            result.extend(list1[p1:])
            return result

        if list1[p1] < list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    return result


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
