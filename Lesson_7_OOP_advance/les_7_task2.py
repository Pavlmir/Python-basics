# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
from abc import ABC, abstractmethod


# Шаблон одежды
class Clothes(ABC):
    def __init__(self):
        self.name = ""
        self.square = 0

    @abstractmethod
    def get_square(self, arg):
        pass

    def __str__(self):
        return f'Расхода ткани на {self.name} {self.square}'


# Потомок класса одежды - пальто
class Coat(Clothes):
    def __init__(self, size):
        self.name = "пальто"
        self.square = self.get_square(size)

    def get_square(self, size):
        return round(size / 6.5 + 0.5)


# Потомок класса одежды - костюм
class Suit(Clothes):
    def __init__(self, height):
        self.name = "костюм"
        self.square = self.get_square(height)

    def get_square(self, height):
        return round(height * 2 + 0.3)


# Класс для расчета суммарного расхода ткани на производство одежды
class CalculationCloth:
    def __init__(self, size, height):
        self.coat_obj = Coat(size)
        self.suit_obj = Suit(height)

    def __str__(self):
        return str(self.coat_obj) + "\n" + str(self.suit_obj)

    @property
    def get_sq_full(self):
        return str(f'Общий расхода ткани: {self.coat_obj.square + self.suit_obj.square}')


cloth_obj = CalculationCloth(13, 9)
print(cloth_obj)
print(cloth_obj.get_sq_full)
