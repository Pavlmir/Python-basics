# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title} - запуск отрисовки: ", end=" ")


class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f"нарисован круг")


class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f"нарисован квадрат")


class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f"нарисован треугольник")


obj_stationery = Stationery("любой канцелярский предмет")
obj_stationery.draw()

print()

obj_pen = Pen("красная ручка")
obj_pen.draw()

obj_pencil = Pencil("зеленый карандаш")
obj_pencil.draw()

obj_handle = Handle("синий маркер")
obj_handle.draw()
