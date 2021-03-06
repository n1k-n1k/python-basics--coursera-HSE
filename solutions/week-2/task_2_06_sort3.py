'''
Упорядочить три числа
Дано три числа. Упорядочите их в порядке неубывания.
Программа должна считывать три числа a,b,c, затем программа должна менять
их значения так, чтобы стали выполнены условия a≤b≤c,
затем программа выводит тройку a,b,c.

Примечания.
Дополнительные ограничения: нельзя использовать дополнительные переменные,
то есть единственной допустимой операцией присваивания является обмен значений
двух переменных типа (a, b) = (b, a). Кстати, аналогично можно делать
присваивания любого количества переменных.

Например, ввод в этой задаче можно оформить так:
a, b, c = int(input()), int(input()), int(input())
'''

a, b, c = int(input()), int(input()), int(input())

if c < a:
    a, c = c, a
if c < b:
    b, c = c, b
if b < a:
    a, b = b, a

print(a, b, c)
