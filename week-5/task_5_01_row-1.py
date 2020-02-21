'''
Ряд - 1

Даны два целых числа A и B (при этом A≤B).
Выведите все числа от A до B включительно.
'''

first, last = int(input()), int(input())

for i in range(first, last + 1):
    print(i, end=' ')
