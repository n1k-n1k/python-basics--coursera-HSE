'''
Разворот последовательности

Дана последовательность целых чисел, заканчивающаяся числом 0.
Выведите эту последовательность в обратном порядке.
При решении этой задачи нельзя пользоваться массивами
и прочими динамическими структурами данных.

Рекурсия вам поможет.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0.
'''


def rev_seq():
    n = int(input())
    if n != 0:
        rev_seq()
        print(n)
    else:
        print(n)


rev_seq()
