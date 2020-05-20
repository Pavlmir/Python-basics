# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg_1, arg_2, arg_3):
    if arg_1 <= arg_2 and arg_1 <= arg_3:
        sum_arg = arg_2 + arg_3
    elif arg_2 <= arg_1 and arg_2 <= arg_3:
        sum_arg = arg_1 + arg_3
    elif arg_3 <= arg_1 and arg_3 <= arg_2:
        sum_arg = arg_1 + arg_2

    return print(f"Наибольшая сумма двух аргументов = {sum_arg}")


a = int(input("Введите 1-ое число: "))
b = int(input("Введите 2-ое число: "))
c = int(input("Введите 3-ое число: "))
my_func(a, b, c)
