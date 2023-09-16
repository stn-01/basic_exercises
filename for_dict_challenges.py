# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = dict()
for student in students:
    names[student['first_name']] = students.count(student)
for key, value in names.items():
    print(f'{key}: {value}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = []
for student in students:
    for key in student:
        names.append(student[key])
counter = 0
most_common_name = ''
for name in names:
    if names.count(name) > counter:
        most_common_name = name
        counter = names.count(name)
print(f'Самое частое имя среди учеников: {most_common_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],

    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for class_ in school_students:
    names_in_class = []
    name_counter = 0
    most_common_name = ''
    for name in class_:
        names_in_class.append(name['first_name'])
        if names_in_class.count(name['first_name']) > name_counter:
            name_counter = names_in_class.count(name['first_name'])
            most_common_name = name['first_name']
    print(f'Самое частое имя в классе {school_students.index(class_) + 1}: {most_common_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [

    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


for class_ in school:
    girls = 0
    boys = 0
    for names in class_['students']:
        if is_male[names['first_name']] == True:
            boys += 1
        else:
            girls += 1
    print(f"Класс {class_['class']}: девочки {girls}, мальчики {boys}")



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
most_girls = [0, '']
most_boys = [0, '']
for class_ in school:
    girls = 0
    boys = 0
    for names in class_['students']:
        if is_male[names['first_name']] == True:
            boys += 1
        else:
            girls += 1
    if boys > most_boys[0]:
        most_boys[0] = boys
        most_boys[1] = class_['class']
    if girls > most_boys[0]:
        most_girls[0] = girls
        most_girls[1] = class_['class']

print(f"Больше всего мальчиков в классе {most_boys[1]}")
print(f"Больше всего девочек в классе {most_girls[1]}")


