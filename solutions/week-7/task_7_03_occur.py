'''
Встречалось ли число раньше

Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO,
если не встречалось.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
'''

lst = input().split()
uniqs = set()

for n in lst:
    print('YES' if n in uniqs else 'NO')
    uniqs.add(n)
