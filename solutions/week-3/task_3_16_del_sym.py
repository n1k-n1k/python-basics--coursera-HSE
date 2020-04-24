'''
Удаление символа

Дана строка.
Удалите из этой строки все символы @.
'''

s = input()
excess_sym = '@'
s = s.replace(excess_sym, '')
print(s)
