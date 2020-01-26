'''
Стоимость покупки

Пирожок в столовой стоит A рублей и B копеек.
Определите, сколько рублей и копеек нужно заплатить за N пирожков.
Программа получает на вход три числа:
A, B, N — целые, неотрицательные, не превышают 10000.
Программа должна вывести два числа: стоимость покупки в рублях и копейках.
'''

rub_per_cake = int(input())
kop_per_cake = int(input())
cakes = int(input())

cakes_cost_kop = (rub_per_cake * 100 + kop_per_cake) * cakes
total_rub = cakes_cost_kop // 100
total_kop = cakes_cost_kop % 100

print(total_rub, total_kop)
