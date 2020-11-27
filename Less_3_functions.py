# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def lesson_1():
    def my_division(arg_1, arg_2):
        if arg_2 == 0:
            return print("Деление на 0!")
        else:
            return print(f"Результат деления = {arg_1 / arg_2}")

    a = int(input("Введите 1-ое число: "))
    b = int(input("Введите 2-ое число: "))
    my_division(a, b)


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def lesson_2():
    def user_data(name, lastname, year_birth, city, email, mobile_number):
        return print(f"Имя - {name}, фамилия - {lastname}, год рождения - {year_birth}, город проживания - {city},"
                     f" email - {email}, телефон - {mobile_number}")

    my_name = "Павел"
    my_lastname = "Гоняев"
    my_year_birth = "1989"
    my_city = "Иркутск"
    my_email = "email@gmail.com"
    my_mobile_number = "+79001234455"
    user_data(name=my_name, lastname=my_lastname, year_birth=my_year_birth, city=my_city, email=my_email,
              mobile_number=my_mobile_number)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def lesson_3():
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


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def lesson_4():
    def my_func1(x, y):
        return print(f" 1-ый вариант, возведение числа x в степень y = {x ** y}")

    def my_func2(x, y):
        result = 1
        for i in range(abs(y)):
            result = result * x
        return print(f" 2-ой вариант, возведение числа x в степень y = {1 / result}")

    x_ = int(input("Введите положительное число: "))
    y_ = int(input("Введите целое отрицательное число: "))
    my_func1(x_, y_)
    my_func2(x_, y_)


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def lesson_5():
    def my_func():
        number_list = []
        exit_program = False
        while not exit_program:
            number = input("Введите строку чисел, разделенных пробелом: ")
            number_list_str = number.split()
            for x in number_list_str:
                if x == "q":
                    exit_program = True
                    break
                else:
                    number_list.append(int(x))
            print(f"Cумма чисел = {sum(number_list)}")

        return print("Программа завершена")

    my_func()


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
def lesson_6():
    def int_func(word):
        new_word_total = ""
        word_list = word.split()
        for word_ in word_list:
            new_word = ""
            for x in word_:
                if 97 <= ord(x) <= 122:
                    new_word = new_word + x
                else:
                    print(f"Пропущена другая буква! - {x}")
            new_word_total = new_word_total + new_word.title() + " "
        return new_word_total

    print(int_func("text"))


if __name__ == "__main__":
    lesson_1()
