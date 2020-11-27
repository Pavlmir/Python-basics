# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("list employees.txt", "r", encoding='UTF-8') as file:
    average_income = 0
    number_employees = 0
    low_income = []
    for line in file:
        line_list = line.split()
        salary = int(line_list[1])
        last_name = line_list[0]
        average_income = average_income + salary
        number_employees = number_employees + 1
        if salary < 20000:
            low_income.append(last_name)

print(f"Сотрудники имеющие оклад менее 20 тыс.: {', '.join(low_income)}")
print(f"Средняя величина дохода сотрудников = {average_income / number_employees:.2f}")
