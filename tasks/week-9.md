## Week-9
## Классы.

*Примечания:*
* *В задачах  курса не нужно проверять ограничения входных данных: гарантируется, что введут данные, соответствующие условию.* 
* *Во всех задачах курса решения должны выдавать в точности требуемый ответ.*


#### Task 9-01: Класс
Реализуйте класс `Matrix`. Он должен содержать:
* Конструктор от списка списков. Гарантируется, что списки состоят из чисел, не пусты и все имеют одинаковый размер. 
Конструктор должен копировать содержимое списка списков, т. е. при изменении списков, от которых была сконструирована матрица, 
содержимое матрицы изменяться не должно.
* Метод `__str__`, переводящий матрицу в строку. При этом элементы внутри одной строки должны быть разделены знаками табуляции, 
а строки — переносами строк. После каждой строки не должно быть символа табуляции и в конце не должно быть переноса строки.
* Метод `size` без аргументов, возвращающий кортеж вида (число строк, число столбцов). 
Пример теста с участием этого метода есть в следующей задаче этой недели.

***Как сдавать задачи этой недели?***

На проверку вы должны сдать только файл, содержащий описание класса и одну строку вне класса (в качестве основной программы):
```
exec(stdin.read())
```
И еще одну строку в начале файла:
```
from sys import stdin
```

Для тестирования класса вы можете вместо строки `exec(stdin.read())` вставлять код из примеров или писать свой код.

Формат ввода: Вводится исходный код тестирующей программы на языке `Python`.

Формат вывода: Выведите результат её работы в текущем окружении при помощи `exec`, как это указано в условии.


#### Task 9-02: Добавить, умножить
Добавьте в предыдущий класс следующие методы:
* `__add__`, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
* `__mul__`, принимающий число типа `int` или `float` и возвращающий матрицу, умноженную на скаляр.
* `__rmul__`, делающий то же самое, что и `__mul__`. 
Этот метод будет вызван в том случае, аргумент находится справа. 
Для реализации этого метода в коде класса достаточно написать `__rmul__ = __mul__`.

Иллюстрация:
* В следующем случае вызовется `__mul__`: `Matrix([[0, 1], [1, 0]) * 10`.
* В следующем случае вызовется `__rmul__` (так как у int не определен `__mul__` для матрицы справа): `10 * Matrix([[0, 1], [1, 0])`.

***Разумеется, данные методы не должны менять содержимое матрицы.***

Формат ввода: Как в предыдущей задаче.

Формат вывода: Как в предыдущей задаче.


#### Task 9-03: Ошибки, транспонирование
Добавьте в программу из предыдущей задачи класс `MatrixError`, содержащий внутри `self` поля `matrix1` и `matrix2` — ссылки на матрицы.

В класс `Matrix` внесите следующие изменения:
* Добавьте в метод `__add__ `проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы разных размеров 
было выброшено исключение `MatrixError` таким образом, чтобы `matrix1` поле `MatrixError` стало первым аргументом `__add__` (просто `self`), 
а `matrix2` — вторым (второй операнд для сложения).
* Реализуйте метод `transpose`, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр класса `Matrix`).
* Реализуйте *статический* метод `transposed`, принимающий `Matrix` и возвращающий транспонированную матрицу. 

Формат ввода: Как в предыдущей задаче.

Формат вывода: Как в предыдущей задаче.
