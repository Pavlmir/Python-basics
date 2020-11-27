# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class MyDay:
    def __init__(self, str_day):
        self.str_day = str_day

    @classmethod
    def number_day(cls, str_day):
        return [int(x) for x in str_day.split("-")]

    @staticmethod
    def check_data_day(day, month, year):
        result = ""
        if not (1 <= day <= 31):
            result = "Неправильный день"

        if not (1 <= month <= 12):
            result = "Неправильный месяц"

        if not (0 <= year <= 2030):
            result = "Неправильный год"

        return result if result else "Все ок"


print(MyDay.number_day("12-12-2020"))
print(MyDay.check_data_day(12, 12, 2020))
