'''
Ряд - 2

Даны два целых числа A и В.
Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
или в порядке убывания в противном случае.
'''

first, last = int(input()), int(input())

direction = 1 if first < last else -1
for i in range(first, last + direction, direction):
    print(i, end=' ')
