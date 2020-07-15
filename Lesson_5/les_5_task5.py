# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("set of numbers.txt", "w", encoding='UTF-8') as file:
    numbers = [1, 2, 3, 56, 7, 21]
    for line in numbers:
        file.write(str(line) + " ")

with open("set of numbers.txt", "r", encoding='UTF-8') as file:
    for line in file:
        numbers = [int(x) for x in line.split()]

print(f"Сумма чисел в файле = {sum(numbers)}")
