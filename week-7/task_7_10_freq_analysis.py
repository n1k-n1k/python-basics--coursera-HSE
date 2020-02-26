'''
Частотный анализ

Дан текст.
Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке.
'''

import sys

words = dict()
for line in sys.stdin.readlines():
    for w in line.split():
        words[w] = words.get(w, 0) + 1

for w, f in sorted(words.items(), key=lambda x: (-x[1], x[0])):
    print(w)
