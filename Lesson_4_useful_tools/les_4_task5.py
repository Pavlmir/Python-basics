# 5. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


from itertools import count
from itertools import cycle
from sys import argv

script_name, start_number_arg1, my_string_arg2 = argv


def integers_starting(start_number):
    start_number = int(start_number)
    for el in count(start_number):
        if el > start_number + 7:
            break
        else:
            print(el)


def repeating_list(my_string):
    с = 0
    for el in cycle(my_string):
        if с > (len(my_string)) * 2 - 1:
            break
        print(el)
        с += 1


print("Имя скрипта: ", script_name)
print("Начало генератора: ", start_number_arg1)
print("Список: ", my_string_arg2)
print(f"а) итератор, генерирующий целые числа, начиная с указанного {start_number_arg1}:")
print(integers_starting(start_number_arg1))
print(f"б) итератор, повторяющий элементы некоторого списка, определенного заранее: {my_string_arg2}")
print(repeating_list(my_string_arg2))
