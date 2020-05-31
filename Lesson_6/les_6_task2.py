# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_mass(self, mass_asphalt, thickness):
        total_mass = self._length * self._width * mass_asphalt * thickness
        print(f"Масса асфальта: {self._length}м * {self._width}м * {mass_asphalt}кг * {thickness}см ="
              f" {total_mass / 1000:.2f} т.")


r = Road(20, 5000)
r.calculation_mass(25, 5)
