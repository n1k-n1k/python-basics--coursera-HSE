'''
Проценты

Процентная ставка по вкладу составляет P процентов годовых,
которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек.
Определите размер вклада через год.

При решении этой задачи нельзя пользоваться условными инструкциями и циклами.
Формат ввода: Программа получает на вход целые числа P, X, Y.
Формат вывода: Программа должна вывести два числа: величину вклада через год
в рублях и копейках. Дробная часть копеек отбрасывается.
'''

p, x, y = int(input()), int(input()), int(input())

dep = (x + y / 100) * (1 + p / 100)
dep_rub = int(dep)
dep_kop = int((dep - dep_rub) * 100 + 0.0001)

print(dep_rub, dep_kop)
