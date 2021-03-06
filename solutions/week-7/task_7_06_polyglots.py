'''
Полиглоты

Каждый из N школьников некоторой школы знает Mᵢ языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

Формат ввода
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк,
содержащих названия языков, которые знает i-й школьник.
Длина названий языков не превышает 1000 символов,
количество различных языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.

Формат вывода
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
'''

n = int(input())
studs = []

for _ in range(n):
    m = int(input())
    languages = []
    for _ in range(m):
        languages.append(input())
    studs.append(set(languages))

languages_all = studs[0].copy()
languages_any = studs[0].copy()

for s in studs[1:]:
    languages_all &= s
    languages_any |= s

print(len(languages_all))
print(*languages_all, sep='\n')
print(len(languages_any))
print(*languages_any, sep='\n')
