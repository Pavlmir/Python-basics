# 1. Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
name = input("Введите имя:")
old = int(input("Ваш возвраст:"))
print(f"Вас зовут {name}, вам {old} лет")

x1 = int(input(f"{name} введи 1-ю переменную:"))
x2 = int(input(f"{name} введи 2-ю переменную:"))
x3 = int(input(f"{name} введи 3-ю переменную:"))
print(f"Сумма переменных = {x1 + x2 + x3}")
