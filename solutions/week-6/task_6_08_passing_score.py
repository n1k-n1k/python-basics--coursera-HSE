'''
Проходной балл

Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов
в виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов.
При этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку)
по любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют
в конкурсе по сумме баллов за три экзамена.

В конкурсе участвует N человек, при этом количество мест равно K.
Определите проходной балл, то есть такое количество баллов, что количество
участников, набравших столько или больше баллов не превосходит K, а при
добавлении к ним абитуриентов, набравших наибольшее количество баллов среди
непринятых абитуриентов, общее число принятых абитуриентов станет больше K.

Формат ввода
Программа получает на вход количество мест K.
Далее идут строки с информацией об абитуриентах, каждая из которых состоит
из имени (текстовая строка содержащая произвольное число пробелов)
и трех чисел от 0 до 100, разделенных пробелами.

Используйте для ввода файл input.txt с указанием кодировки utf8
(для создания такого файла на своем компьютере в программе Notepad++
следует использовать кодировку UTF-8 без BOM).

Формат вывода
Программа должна вывести проходной балл в конкурсе.
Выведенное значение должно быть минимальным баллом,
который набрал абитуриент, прошедший по конкурсу.

Также возможны две ситуации, когда проходной балл не определен.
Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок,
программа должна вывести число 0.

Если количество имеющих равный максимальный балл абитуриентов больше чем K,
программа должна вывести число 1.

Используйте для вывода файл output.txt с указанием кодировки utf8.
'''


def get_all_applicants(path):
    applicants = []
    with open(path, 'r', encoding='utf8') as f:
        places = int(f.readline())
        for line in f.readlines():
            st = line.split()
            sc = list(map(int, st[-3:]))
            name = ' '.join(st[:-3])
            applicants.append([name, sc[0], sc[1], sc[2]])
    return places, applicants


def passing_score(path):
    places, applicants_all = get_all_applicants(path)
    applicants = []
    scores = []
    for st in applicants_all:
        name = st[0]
        sc_total = sum(st[1:])
        if st[1] >= 40 and st[2] >= 40 and st[3] >= 40:
            applicants.append([name, sc_total])
            scores.append(sc_total)
    applicants.sort(key=lambda x: x[1], reverse=True)

    if len(applicants) <= places:
        return 0

    max_sc = applicants[0][1]
    max_sc_count = scores.count(max_sc)
    if max_sc_count > places:
        return 1
    if max_sc_count == places:
        return applicants[0][1]

    while applicants[places - 1][1] == applicants[places][1]:
        places -= 1
    return applicants[places - 1][1]


print(passing_score('task_6_08_input_data.txt'))
