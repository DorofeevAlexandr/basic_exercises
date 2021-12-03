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

print('Задание 1')

students_count = {}
for student in students:
    if student['first_name'] in students_count:
        students_count[student['first_name']] += 1
    else:
        students_count[student['first_name']] = 1

# print(students_count)
for name in students_count:
    print(f'{name}: {students_count[name]}')


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

print('Задание 2')

students_count = {}
for student in students:
    if student['first_name'] in students_count:
        students_count[student['first_name']] += 1
    else:
        students_count[student['first_name']] = 1

max_count_name = list(students_count.keys())[0]
for name in students_count:
    if students_count[name] >= students_count[max_count_name]:
        max_count_name = name
    
print(max_count_name)

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
print('Задание 3')

def name_max_students(students):
    students_count = {}
    for student in students:
        if student['first_name'] in students_count:
            students_count[student['first_name']] += 1
        else:
            students_count[student['first_name']] = 1

    max_count_name = list(students_count.keys())[0]
    for name in students_count:
        if students_count[name] >= students_count[max_count_name]:
            max_count_name = name
    
    return max_count_name

for clas_num, students in enumerate(school_students):
    print(f'Самое частое имя в классе {clas_num + 1}: {name_max_students(students)}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

print('Задание 4')
for clas in school:
    clas['male_count'] = 0
    clas['female_count'] = 0

    for student in clas['students']:
        if student['first_name'] in is_male.keys():
            if is_male[student['first_name']]:
                clas['male_count'] += 1
            else:
                clas['female_count'] += 1

    print(f'Класс {clas["class"]}: девочки {clas["female_count"]}, мальчики {clas["male_count"]}')



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

print('Задание 5')

for clas in school:
    clas['male_count'] = 0
    clas['female_count'] = 0

    for student in clas['students']:
        if student['first_name'] in is_male.keys():
            if is_male[student['first_name']]:
                clas['male_count'] += 1
            else:
                clas['female_count'] += 1


max_male_class, max_count_male = school[0]['class'], school[0]['male_count']
max_female_class, max_count_female = school[0]['class'], school[0]['female_count']
for clas in school:
    if clas["male_count"] >= max_count_male:
        max_male_class, max_count_male = clas['class'], clas['male_count']
    if clas["female_count"] >= max_count_female:
        max_female_class, max_count_female = clas['class'], clas['female_count']

print(f'Больше всего мальчиков в классе {max_male_class}')
print(f'Больше всего девочек в классе {max_female_class}')
