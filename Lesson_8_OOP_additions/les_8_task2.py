# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnZeroDivisionError(ZeroDivisionError):
    def __str__(self):
        return "На ноль делить нельзя!"

    @staticmethod
    def division(x, y):
        try:
            if y == 0:
                raise OwnZeroDivisionError()
            return x / y
        except OwnZeroDivisionError as err:
            return err


print(OwnZeroDivisionError.division(4, 0))
