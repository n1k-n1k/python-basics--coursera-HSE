## Week-8
## Функциональное программирование.

*Примечания:*
* *В задачах  курса не нужно проверять ограничения входных данных: гарантируется, что введут данные, соответствующие условию.* 
* *Во всех задачах курса решения должны выдавать в точности требуемый ответ.*


#### Task 8-01: Количество различных чисел
Дан список чисел, который может содержать до 100 000 чисел.

Определите, сколько в нем встречается различных чисел.

Формат ввода: Вводится список целых чисел. Все числа списка находятся на одной строке.


#### Task 8-02: Количество слов в тексте
Во входном файле (вы можете читать данные из `sys.stdin`, подключив библиотеку `sys`) записан текст. 

Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки. 

Определите, сколько различных слов содержится в этом тексте.


#### Task 8-03: Наименьший нечетный
Выведите значение наименьшего нечетного элемента списка, гарантируется, что хотя бы один нечётный элемент в списке есть.

Формат ввода: Вводится список чисел. Все числа списка находятся на одной строке.


#### Task 8-04: Ноль или не ноль
Проверьте, есть ли среди данных `N` чисел нули.

Формат ввода: Вводится число `N`, а затем `N` чисел.

Формат вывода: Выведите `True`, если среди введенных чисел есть хотя бы один нуль, или `False` в противном случае.


#### Task 8-05: Произведение пятых степеней
На вход подаётся последовательность натуральных чисел длины `n ≤ 1 000`.

Посчитайте произведение пятых степеней чисел в последовательности.

Формат ввода: Вводится последовательность чисел

Формат вывода: Выведите ответ на задачу

*Примечания: Для решения задачи используйте функцию reduce из модуля `functools`*


#### Task 8-06: XOR
Булева функция `XOR` (сложение по модулю два) задаётся следующей таблицей истинности:

* `xor(0, 0) = 0`
* `xor(0, 1) = 1`
* `xor(1, 0) = 1`
* `xor(1, 1) = 0`

На вход подаются две последовательности `(a₁, …, an)` и `(b₁, …, bn)` из 0 и 1.

Вычислите последовательность из `(c₁, …, cn)`, где каждая `cᵢ = xor(aᵢ, bᵢ)`.

Формат ввода: На вход подаются две строки из 0 и 1, разделённых пробелами.

Первая строка — это последовательность `(a₁, …, an)`.

Вторая строка — это последовательность `(b₁, …, bn)`.

Формат вывода: Выведите последовательность `(c₁, …, cn)`, разделяя каждый элемент пробелом

*Примечания: Для решения задачи можете использовать функцию `zip`.*
