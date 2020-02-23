'''
Отсортировать список участников по алфавиту

Известно, что фамилии всех участников — различны.
Сохраните в массивах список всех участников и выведите его, отсортировав
по фамилии в лексикографическом порядке. При выводе указываете фамилию,
имя участника и его балл.

Используйте для ввода и вывода файлы input.txt и output.txt
с указанием кодировки utf8. Например, для чтения откройте файл
с помощью open('input.txt', 'r', encoding='utf8').

Входные данные
Строки вида "Фамилия Имя НомерШколы Балл".

Выходные данные
Строки вида "Фамилия Имя Балл", отсортированные по фамилии.
'''


def read_students(path):
    students = []
    with open(path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            students.append(line.split())
    return students


def write_students(path, students):
    with open(path, 'w', encoding='utf8') as f:
        for s in sorted(students):
            print(s[0], s[1], s[3], file=f)


stds = read_students('task_6_05_input_data.txt')
write_students('task_6_05_output_data.txt', stds)
