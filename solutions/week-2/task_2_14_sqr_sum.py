'''
Сумма квадратов

По данному натуральному n вычислите сумму 1²+2²+3²+...+n².
'''

n = int(input())
i = 1
sqr_sum = 0

while i <= n:
    sqr_sum += i ** 2
    i += 1

print(sqr_sum)
