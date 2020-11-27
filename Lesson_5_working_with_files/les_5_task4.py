# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("counting.txt", "r", encoding='UTF-8') as file:
    translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    new_list = []
    for line in file:
        line_list = line.split()
        new_line = translate.get(line_list[0]) + " " + " ".join(line_list[1:])
        new_list.append(new_line)

with open("counting_new.txt", "w", encoding='UTF-8') as file:
    for line in new_list:
        file.write(line + "\n")
