# 3. Реализовать программу работы с органическими клетками.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Органическая клетка - Количество ячеек клетки {self.quantity} = {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else 'Отрицательно!'

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}' + "\n "
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(9)
cells2 = Cell(13)
print(cells1)
print(cells2)
print("Сложение:", cells1 + cells2)
print("Вычитание:", cells2 - cells1)
print("Умножение:", cells2 * cells1)
print("Организовать ячейки по рядам:\n", cells1.make_order(3))
print("Организовать ячейки по рядам:\n", cells2.make_order(4))
print("Деление:", cells1 / cells2)
