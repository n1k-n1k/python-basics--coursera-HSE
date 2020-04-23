## Week-4
## Функции и рекурсия.

*Примечания:*
* *В задачах  курса не нужно проверять ограничения входных данных: гарантируется, что введут данные, соответствующие условию.* 
* *Во всех задачах курса решения должны выдавать в точности требуемый ответ.*


#### Task 4-01: Минимум 4 чисел
Напишите функцию `min4(a, b, c, d)`, вычисляющую минимум четырех чисел, которая не содержит инструкции `if`, а использует стандартную функцию min от двух чисел. Считайте четыре целых числа и выведите их минимум.

Формат ввода: Вводятся четыре целых числа.


#### Task 4-02: Принадлежит ли точка квадрату - 1
Даны два действительных числа `x` и `y`. 

Проверьте, принадлежит ли точка с координатами `(x, y)` заштрихованному квадрату (включая его границу). 

Если точка принадлежит квадрату, выведите слово `YES`, иначе выведите слово `NO`. 
На рисунке сетка проведена с шагом 1.
 
Решение должно содержать функцию `IsPointInSquare(x, y)`, возвращающую `True`, если точка принадлежит квадрату и `False`, если не принадлежит. 

Основная программа должна считать координаты точки, вызвать функцию `IsPointInSquare` и в зависимости от возвращенного значения вывести на экран необходимое сообщение. 
Функция `IsPointInSquare` не должна содержать инструкцию `if`.

Формат ввода: Вводятся два действительных числа.


#### Task 4-03: Принадлежит ли точка кругу
Даны пять действительных чисел: `x`, `y`, `xc`, `yc`, `r`.

Проверьте, принадлежит ли точка `(x,y)` кругу с центром `(xc, yc)` и радиусом `r`.

Если точка принадлежит кругу, выведите слово `YES`, иначе выведите слово `NO`.

Решение должно содержать функцию `IsPointInCircle(x, y, xc, yc, r)`, возвращающую `True`, если точка принадлежит кругу и `False`, если не принадлежит.

Основная программа должна считать координаты точки, вызвать функцию `IsPointInCircle` и в зависимости от возвращенного значения вывести на экран необходимое сообщение. 

Функция `IsPointInCircle` не должна содержать инструкцию `if`.

Формат ввода: Вводится пять действительных чисел.


#### Task 4-04: Минимальный делитель числа
Дано натуральное число `n > 1`. 

Выведите его наименьший делитель, отличный от 1. Решение оформите в виде функции `MinDivisor(n)`.
 
Алгоритм должен иметь сложность порядка корня квадратного из `n`.

*Указание. Если у числа `n` нет делителя не превосходящего корня из `n`, то число `n` — простое и ответом будет само число `n`. 
А у всех составных чисел обязательно есть делители, отличные от единицы и не превосходящие корня из `n`.*

Формат ввода: Вводится натуральное число.
 

#### Task 4-05: Проверка числа на простоту
Дано натуральное число `n > 1`. Проверьте, является ли оно простым. 

Программа должна вывести слово `YES`, если число простое и `NO`, если число составное. 

Решение оформите в виде функции `IsPrime(n)`, которая возвращает `True` для простых чисел и `False` для составных чисел. 

Программа должна иметь сложность `O(корень из n)`: количество действий в программе должно быть пропорционально квадратному корню из `n` (иначе говоря, при увеличении входного числа в `k` раз, время выполнения программы должно увеличиваться примерно в `корень из k раз`).

Формат ввода: Вводится натуральное число.
 

#### Task 4-06: Возведение в степень

Дано действительное положительное число a и целое неотрицательное число `n`. 

Вычислите `aⁿ`, не используя циклы и стандартную функцию pow, но используя рекуррентное соотношение `aⁿ=a⋅aⁿ⁻¹`.

Решение оформите в виде функции `power(a, n)` (которая возвращает `aⁿ`).

Формат ввода: Вводятся действительное положительное число `a` и целое неотрицательное число `n`.

Формат вывода: Выведите ответ на задачу: `print(power(a, n))`.


#### Task 4-07: Сложение без сложения
Напишите рекурсивную функцию `sum(a, b)`, возвращающую сумму двух целых неотрицательных чисел. 

Из всех арифметических операций допускаются только `+1` и `-1`. Также нельзя использовать циклы.

Формат ввода: Вводятся два удовлетворяющих условию задачи числа. Числа не превышают 900.


#### Task 4-08: Быстрое возведение в степень
Возводить в степень можно гораздо быстрее, чем за `n` умножений! 

Для этого нужно воспользоваться следующими рекуррентными соотношениями: 
`aⁿ = (a²)ⁿ/²` при четном `n`, `aⁿ=a⋅aⁿ⁻¹` при нечетном `n`. 

Реализуйте алгоритм быстрого возведения в степень. 
Если вы все сделаете правильно, то сложность вашего алгоритма будет `O(logn)`.

Формат ввода: Вводится действительное число `a` и целое неотрицательное число `n`.


#### Task 4-09: Сократите дробь
Даны два натуральных числа `n` и `m`.

Сократите дробь `(n / m)`, то есть выведите два других числа `p` и `q` таких, что `(n / m) = (p / q)` и дробь `(p / q)` — несократимая.

Решение оформите в виде функции `ReduceFraction(n, m)`, получающая значения `n` и `m` и возвращающей кортеж из двух чисел: `return p, q`.

Тогда вывод можно будет оформить как `print(*ReduceFraction(n, m))`.

Формат ввода: Вводятся два натуральных числа.


#### Task 4-10: Сумма последовательности
Дана последовательность чисел, завершающаяся числом `0`. 

Найдите сумму всех этих чисел, не используя цикл.

Формат ввода: Вводится последовательность целых чисел, оканчивающаяся числом `0` (само число `0` в последовательность не входит, а служит как признак ее окончания).
 

#### Task 4-11: Разворот последовательности
Дана последовательность целых чисел, заканчивающаяся числом `0`. 

Выведите эту последовательность в обратном порядке. 

При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных. **Рекурсия вам поможет.**

Формат ввода: Вводится последовательность целых чисел, оканчивающаяся числом `0`.
