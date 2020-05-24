# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

script_name, production_in_hours_arg1, rate_hour_arg2, bonus_arg3 = argv


def salary_accounting(production_in_hours, rate_hour, bonus):
    return (int(production_in_hours) * int(rate_hour)) + int(bonus)


print("Имя скрипта: ", script_name)
print("Выработка в часах: ", production_in_hours_arg1)
print("Ставка в час: ", rate_hour_arg2)
print("Премия: ", bonus_arg3)
print("Заработная плата сотрудника = ", salary_accounting(production_in_hours_arg1, rate_hour_arg2, bonus_arg3))
