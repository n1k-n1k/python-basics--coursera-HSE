## Week-2
### Условный оператор и цикл while

*Примечания:*
* *В задачах  курса не нужно проверять ограничения входных данных: гарантируется, что введут данные, соответствующие условию.* 
* *Во всех задачах курса решения должны выдавать в точности требуемый ответ.*


#### Task 2-01: Максимум из двух
Напишите программу, которая считывает два целых числа A и B и выводит наибольшее значение из них. 
Числа — целые от 1 до 1000.


#### Task 2-02: Какое число больше?
Даны два целых числа. Программа должна вывести число "1", если первое число больше второго, 
число "2", если второе больше первого или число "0", если они равны.

*Примечание: Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.*


#### Task 2-03: Максимум трех чисел
Даны три целых числа. 
Найдите наибольшее из них (программа должна вывести ровно одно целое число).

Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для решения этой задачи?


#### Task 2-04: Високосный год
Дано натуральное число. 
Требуется определить, является ли год с данным номером високосным. 

Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, или же если он кратен 400.


#### Task 2-05: Коровы
Для данного числа n<100 закончите фразу “На лугу пасется...” одним из возможных продолжений: 
“n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

Формат ввода:
Вводится натуральное число.

Формат вывода:
Программа должна вывести введенное число n и одно из слов: korov, korova или korovy. 
Между числом и словом должен стоять ровно один пробел.


#### Task 2-06: Упорядочить три числа
Дано три числа. Упорядочите их в порядке неубывания. 
Программа должна считывать три числа a,b,c, затем программа должна менять их значения так, 
чтобы стали выполнены условия a≤b≤c, затем программа выводит тройку a,b,c.

*Примечания. Дополнительные ограничения: нельзя использовать дополнительные переменные, 
то есть единственной допустимой операцией присваивания является обмен значений двух переменных типа (a, b) = (b, a). 
Кстати, аналогично можно делать присваивания любого количества переменных. 
Например, ввод в этой задаче можно оформить так:*

`a, b, c = int(input()), int(input()), int(input())`


#### Task 2-07: Сколько совпадает чисел
Даны три целых числа. Определите, сколько среди них совпадающих. 

Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).


#### Task 2-08: Узник замка Иф
За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D×E. 
Замок Иф сложен из кирпичей, размером A×B×C. 

Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие 
(очевидно, стороны кирпича должны быть параллельны сторонам отверстия).

Формат ввода:
Программа получает на вход числа A, B, C, D, E.

Формат вывода:
Программа должна вывести слово YES или NO.


#### Task 2-09: Коробки
Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂. 

Определите, можно ли разместить одну из этих коробок внутри другой, при условии, 
что поворачивать коробки можно только на 90 градусов вокруг ребер.

Формат ввода:
Программа получает на вход числа A₁,B₁,C₁,A₂,B₂,C₂.

Формат вывода:
Программа должна вывести одну из следующих строчек:

* `Boxes are equal`, если коробки одинаковые,
* `The first box is smaller than the second one`, если первая коробка может быть положена во вторую,
* `The first box is larger than the second one`, если вторая коробка может быть положена в первую,
* `Boxes are incomparable`, во всех остальных случаях.


#### Task 2-10: Список квадратов
По данному целому числу N распечатайте все квадраты натуральных чисел,не превосходящие N, в порядке возрастания.


#### Task 2-11: Минимальный делитель
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

Формат ввода:
Вводится целое положительное число.


#### Task 2-12: Утренняя пробежка
В первый день спортсмен пробежал X километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения 
(для решения задачи разрешается использовать числа с запятой, которые в Питоне пишутся через точку).

По данному числу X определите номер дня, на который пробег спортсмена составит не менее Y километров.

Формат ввода:
Программа получает на вход числа X и Y.


#### Task 2-13: Максимум последовательности
Последовательность состоит из целых чисел и завершается числом 0. 

Определите значение наибольшего элемента последовательности.

Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).


#### Task 2-14: Сумма квадратов
По данному натуральному n вычислите сумму 1²+2²+3²+...+n².


#### Task 2-15: Длина последовательности
Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке. 
Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу 
и вывести количество членов последовательности (не считая завершающего числа 0).

Числа, следующие за числом 0, считывать не нужно.

Формат ввода:
Вводится последовательность целых чисел, заканчивающаяся числом 0.


#### Task 2-16: Сумма последовательности
Определите сумму всех элементов последовательности, завершающейся числом 0.

Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).


#### Task 2-17: Количество четных элементов последовательности
Определите количество четных элементов в последовательности, завершающейся числом 0.

Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).


#### Task 2-18: Второй максимум
Последовательность состоит из натуральных чисел и завершается числом 0. 

Определите значение второго по величине элемента в этой последовательности, то есть элемента, 
который будет наибольшим, если из последовательности удалить одно вхождение наибольшего элемента.

Формат ввода:
Вводится последовательность натуральных чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).


#### Task 2-19: Количество элементов, равных максимуму
Последовательность состоит из натуральных чисел и завершается числом 0. 

Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.

Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).


#### Task 2-20: Максимальное число подряд идущих равных
Дана последовательность натуральных чисел, завершающаяся числом 0. 

Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

Формат ввода:
Вводится последовательность натуральных чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).



#### Train 2-01: Ход короля
*(тренировочное задание)*

Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. 

Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом.

Формат ввода: 
Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

Формат вывода: 
Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую 
или NO в противном случае.


#### Train 2-02: Квартиры
*(тренировочное задание)*

В доме несколько подъездов. В каждом подъезде одинаковое количество квартир. Квартиры нумеруются подряд, начиная с единицы. Может ли в некотором подъезде **первая** квартира иметь номер x, а **последняя** – номер y?

Формат ввода:
Вводятся два натуральных числа x и y (x ≤ y).

Формат вывода:
Выведите слово YES (заглавными латинскими буквами), если такое возможно, и NO в противном случае.


#### Train 2-03: Цвет клеток шахматной доски
*(тренировочное задание)*

Заданы две клетки шахматной доски. 

Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета – то NO.

Формат ввода: 
Вводятся 4 числа - координаты клеток.


#### Train 2-04: Шоколадка
*(тренировочное задание)*

Шоколадка имеет вид прямоугольника, разделенного на n×m долек. 
Шоколадку можно один раз разломить по прямой на две части. 

Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек.

Формат ввода:
Программа получает на вход три числа: n, m, k.

Формат вывода:
Программа должна вывести одно из двух слов: YES или NO.


#### Train 2-05: Знак числа
*(тренировочное задание)*

В математике функция sign(x) (знак числа) определена так:
* sign(x)=1, если x>0,
* sign(x)=-1, если x<0,
* sign(x)=0, если x=0.

Для данного числа x выведите значение sign(x).

Формат ввода:
Вводится одно целое число.

*Примечания. Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.*


#### Train 2-06: Координатные четверти
*(тренировочное задание)*

Даны координаты двух точек на плоскости, требуется определить, лежат ли они в одной координатной четверти или нет 
(все координаты отличны от нуля).

Формат ввода:
Вводятся 4 числа: координаты первой точки (x1,y1) и координаты второй точки (x2,y2).

Формат вывода:
Программа должна вывести слово YES, если точки находятся в одной координатной четверти, в противном случае вывести слово NO.


#### Train 2-07: Шашки
*(тренировочное задание)*

На доске стоит белая шашка. 
Требуется определить, может ли она попасть в заданную клетку, делая ходы по правилам и не пользуясь ходами дамки 
(т. е. не используя возможность перемещаться назад после превращения в дамку). 
Белые шашки могут ходить по клеткам одного цвета по диагонали вверх-влево или вверх-вправо. Ходов может быть несколько!

*Примечания: Доска имеет размер 8x8, вертикали и горизонтали нумеруются числами от 1 до 8 начиная с левого нижнего угла.
 Исходная и конечная клетки не совпадают.*

Формат ввода:
Вводится клетка, где стоит шашка, а затем клетка, куда шашка должна попасть.
Каждая клетка описывается номером вертикали, а затем номером горизонтали. 
Под номером вертикали имеется в виду не номер по вертикали, а номер вертикальной линии считая слева направо. 
Аналогичная формулировка используется для номера горизонтали: нумерация идет снизу вверх. 
Например, клетка A2 кодируется как 1 2.

Формат вывода:
Выведите слово YES (заглавными буквами), если шашка может попасть из начальной клетки в указанную, 
и NO в противном случае.


#### Train 2-08: Тип треугольника
*(тренировочное задание)*

Даны три стороны треугольника a,b,c. Определите тип треугольника с заданными сторонами. 
Выведите одно из четырех слов: rectangular для прямоугольного треугольника, acute для остроугольного треугольника, 
obtuse для тупоугольного треугольника или impossible, если треугольника с такими сторонами не существует 
(считаем, что вырожденный треугольник тоже невозможен).

Формат ввода:
Вводятся три целых числа.


#### Train 2-09: Четные и нечетные
*(тренировочное задание)*

Даны три целых числа A, B, C. Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.

Формат ввода:
Числа A, B, C, не превышающие по модулю 10000.

Формат вывода:
Одна строка – "YES" или "NO".


#### Train 2-10: Складирование ноутбуков
*(тренировочное задание)*

На склад, который имеет форму прямоугольного параллелепипеда, привезли ноутбуки, упакованные в коробки. 
Каждая коробка также имеет форму прямоугольного параллелепипеда. 
По правилам хранения коробки с ноутбуками должны быть размещены на складе с выполнением следующих двух условий:

* Стороны коробок должны быть параллельны сторонам склада.
* Коробку при помещении на склад разрешается расположить где угодно (с выполнением предыдущего условия), 
в том числе на другой коробке, но все коробки должны быть ориентированы одинаково 
(т.е. нельзя одну коробку расположить “стоя”, а другую —“лежа”)

Напишите программу, которая по размерам склада и размерам коробки с ноутбуком определит 
максимальное количество ноутбуков, которое может быть размещено на складе.

Формат ввода:
Программа получает на вход шесть натуральных чисел. Первые три задают длину, высоту и ширину склада. 
Следующие три задают соответственно длину, высоту и ширину коробки с ноутбуком.

Формат вывода:
Программа должна вывести одно число — максимальное количество ноутбуков, которое может быть размещено на складе.


#### Train 2-11: Мороженое
*(тренировочное задание)*

В кафе мороженое продают по три шарика и по пять шариков. Можно ли купить ровно k шариков мороженого?

Формат ввода:
Вводится число k (целое,положительное)

Формат вывода:
Программа должна вывести слово YES, если при таких условиях можно набрать ровно k шариков (не больше и не меньше), в противном случае - вывести NO.


#### Train 2-12: Сложное уравнение*
*(тренировочное задание повышенной сложности)*

Решить в целых числах уравнение: `(ax+b) / (cx+d) = 0`

Формат ввода:
Вводятся 4 числа: a,b,c,d; c и d не равны нулю одновременно.

Формат вывода:
Необходимо вывести все решения, если их число конечно, “NO” (без кавычек), если решений нет, 
и “INF” (без кавычек), если решений бесконечно много.


#### Train 2-13: Котлеты*
*(тренировочное задание повышенной сложности)*

На сковородку одновременно можно положить k котлет. 
Каждую котлету нужно с каждой стороны обжаривать m минут непрерывно. 

За какое наименьшее время удастся поджарить с обеих сторон n котлет?

Формат ввода:
Программа получает на вход три числа: k,m,n.

Формат вывода:
Программа должна вывести одно число: наименьшее количество минут.


#### Train 2-14: Спички*
*(тренировочное задание повышенной сложности)*

Вдоль прямой выложены три спички. Необходимо переложить одну из них так, чтобы при поджигании любой спички 
сгорали все три. Для того чтобы огонь переходил с одной спички на другую, необходимо чтобы эти спички соприкасались 
(хотя бы концами).

Требуется написать программу, определяющую, какую из трех спичек необходимо переместить.

Формат ввода:
Вводятся шесть целых чисел : l₁, r₁, l₂, r₂, l₃, r₃ – координаты первой, второй и третьей спичек соответственно 
(0 ≤ lᵢ < rᵢ ≤ 100). Каждая спичка описывается координатами левого и правого концов по горизонтальной оси OX.

Формат вывода:
Выведите номер искомой спички. Если возможных ответов несколько, то выведите наименьший из них 
(наименьший по номеру спички). В случае, когда нет необходимости перемещать какую-либо спичку, выведите 0. 
Если же требуемого результата достигнуть невозможно, то выведите -1.


#### Train 2-15: Упаковка*
*(тренировочное задание повышенной сложности)*

В одну транспортную компанию поступил заказ на перевозку двух ящиков из одного города в другой. 
Для перевозки ящики решено было упаковать в специальный контейнер.

Ящики и контейнер имеют вид прямоугольных параллелепипедов. Длина, ширина и высота первого ящика — l₁,w₁ и h₁, 
соответствующие размеры второго ящика – l₂,w₂ и h₂. Контейнер имеет длину, ширину и высоту lc,wc и hc.

Поскольку ящики содержат хрупкое оборудование, после упаковки в контейнер каждый из них должен остаться 
в строго вертикальном положении. Таким образом, ящики можно разместить рядом или один на другом. 

Для надежного закрепления в контейнере стороны ящиков должны быть параллельны его сторонам. 
Иначе говоря, если исходно ящики были расположены так, что все их стороны параллельны 
соответствующим сторонам контейнера, то каждый из них разрешается перемещать и поворачивать 
относительно вертикальной оси на угол, кратный 90 градусам (относительно горизонтальной оси ни контейнер, 
ни ящики поворачивать нельзя).

Разумеется, после упаковки оба ящика должны полностью находиться внутри контейнера и не должны пересекаться.

Выясните, можно ли поместить ящики в контейнер с соблюдением указанных условий.

Формат ввода:
Во входных данных записаны числа l₁, w₁, h₁, l₂,w₂, h₂, lc, wc и hc. 
Все размеры — целые положительные числа, не превышающие 1000. Числа в строках разделены пробелами.

#### Train 2-16 Список степеней двойки
*(тренировочное задание)*

По данному числу N распечатайте все целые степени двойки, не превосходящие N, в порядке возрастания.
Операцией возведения в степень пользоваться нельзя!

Формат ввода:
Вводится натуральное число.


#### Train 2-17: Точная степень двойки
*(тренировочное задание)*

Дано натуральное число N. 

Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае. Операцией возведения в степень пользоваться нельзя!

Формат ввода:
Вводится натуральное число.


#### Train 2-18: Двоичный логарифм
*(тренировочное задание)*

По данному натуральному числу N выведите такое наименьшее целое число k, что 2ᵏ≥N.

Операцией возведения в степень пользоваться нельзя!

Формат ввода:
Вводится натуральное число.


#### Train 2-19: Среднее значение последовательности
*(тренировочное задание)*

Определите среднее значение всех элементов последовательности, завершающейся числом 0. 

Использовать массивы в данной задаче нельзя.

Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).


#### Train 2-20: Количество элементов, больше предыдущего
*(тренировочное задание)*

Последовательность состоит из натуральных чисел и завершается числом 0. 

Определите, сколько элементов этой последовательности больше предыдущего элемента.

Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).

#### Train 2-21: Числа Фибоначчи
*(тренировочное задание)*

Последовательность Фибоначчи определяется так:

`F[0] = 0, F[1] = 1, ..., F[n] = F[n-1] + F[n-2].`

По данному числу n определите n-е число Фибоначчи F[n].

Формат ввода:
Вводится натуральное число n.


#### Train 2-22: Номер числа Фибоначчи
*(тренировочное задание)*

Последовательность Фибоначчи определяется так:

`F[0]=0, F[1]=1, ..., F[n]=F[n-1]+F[n-2].`

Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что F[n]=A.

Если А не является числом Фибоначчи, выведите число -1.

Формат ввода:
Вводится натуральное число A.


#### Train 2-23: Исполнитель раздвоитель
*(тренировочное задание)*

Исполнитель “Раздвоитель” преобразует натуральные числа. 
У него есть две команды: “Вычесть 1” и “Разделить на 2”, первая команда уменьшает число на 1, 
вторая команда уменьшает число в два раза, если оно чётное,иначе происходит ошибка. 

Дано два натуральных числа A и B (A>B). 

Напишите алгоритм для Раздвоителя, который преобразует число A в число B и при этом содержит минимальное число команд. 
Команды алгоритма нужно выводить по одной в строке, первая команда обозначается, как -1, вторая команда как :2.

*Примечание. В этой задаче следует переходить из 2 в 1 командой :2. 
Если выполнять переход командой -1, то тестирующая система выдаст вердикт WA.*

Формат ввода:
Вводятся два натуральных числа A и B.


#### Train 2-24: Обращение числа
*(тренировочное задание)*

Переставьте цифры числа в обратном порядке .

Формат ввода:
Задано единственное число N

Формат вывода:
Необходимо вывести цифры данного числа в обратном порядке.


#### Train 2-25: Количество палиндромов
*(тренировочное задание)*

Назовем число палиндромом, если оно не меняется при перестановке его цифр в обратном порядке. 

Напишите программу, которая по заданному числу K выводит количество натуральных палиндромов, не превосходящих K.

Формат ввода:
Задано единственное число K (1≤K≤100000).

Формат вывода:
Необходимо вывести количество натуральных палиндромов, не превосходящих K.

#### Train 2-26: Максимальная длина монотонного фрагмента
*(тренировочное задание)*

Дана последовательность натуральных чисел, завершающаяся числом 0. 

Определите наибольшую длину монотонного фрагмента последовательности 
(то есть такого фрагмента, где все элементы либо больше предыдущего, либо меньше).

Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).


#### Train 2-27: Наименьшее расстояние между локальными максимумами
*(тренировочное задание)*

Определите наименьшее расстояние между двумя локальными максимумами последовательности натуральных чисел, 
завершающейся числом 0. Локальным максимумом называется такое число в последовательности, которое больше своих соседей. 

Если в последовательности нет двух локальных максимумов, выведите число 0. 
Начальное и конечное значение при этом локальными максимумами не считаются.

Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, 
а служит как признак ее окончания).

*Примечания. Пояснение к тестам:*
* *В первом тесте локальными максимумами являются все двойки (они больше соседей). 
Между последними - расстояние наименьшее.*
* *Во втором тесте нет локального максимума.*