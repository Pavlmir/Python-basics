# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


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
