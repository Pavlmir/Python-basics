# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

with open("firm.txt", "r", encoding='UTF-8') as file:
    firm_profit = {}
    firm_loss = {}
    profit_total = 0
    for line in file:
        line_list = line.split()
        revenues = int(line_list[2])
        costs = int(line_list[3])
        if revenues >= costs:
            profit = revenues - costs
            firm_profit[line_list[0]] = profit
            profit_total = profit_total + profit
        else:
            loss = costs - revenues
            firm_loss[line_list[0]] = loss

    firm_average = {"average_profit": profit_total / len(firm_profit)}
    firm = [firm_profit, firm_average]
    if len(firm_loss) != 0:
        firm.append(firm_loss)

with open("firm.json", "w", encoding='UTF-8') as write_f:
    json.dump(firm, write_f)

print(firm)
