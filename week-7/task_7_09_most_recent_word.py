'''
Самое частое слово

Дан текст.
Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше
в лексикографическом порядке.
'''

import sys
words = dict()
for line in sys.stdin.readlines():
    for w in line.split():
        words[w] = words.get(w, 0) + 1

print(sorted(words.items(), key=lambda x: (-x[1], x[0]))[0][0])
