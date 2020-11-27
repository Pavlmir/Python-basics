# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("count lines.txt", "r", encoding='UTF-8') as file:
    n = 0
    for line in file:
        line_list = line.split()
        n = n + 1
        print(f"В строке {n} количество слов = {len(line_list)}")

print(f"Итого строк = {n}")
