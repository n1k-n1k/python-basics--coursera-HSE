'''
Сумма цифр трехзначного числа

Дано трехзначное число. Найдите сумму его цифр.
Вводится целое положительное число.
Гарантируется, что оно соответствует условию задачи.
'''

n = int(input())
dig1 = n % 10
dig2 = (n % 100 - n % 10) // 10
dig3 = (n % 1000 - n % 100) // 100
print(dig1 + dig2 + dig3)
