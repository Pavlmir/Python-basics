# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
from time import sleep
from sys import argv

def lesson_1():
    script_name = argv

    class TrafficLight:
        def __init__(self):
            self.__color = ["красный", "желтый", "зеленый"]

        def running(self):
            data_traffic_light = {"красный": 7, "желтый": 2, "зеленый": 5}

            for x in self.__color:
                sec = data_traffic_light[x]
                print(f"Горит {x}, осталось: {sec} сек.")
                sleep(sec)


    traffic = TrafficLight()
    traffic.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
def lesson_2():
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


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
def lesson_3():
    class Worker:
        def __init__(self, name, surname, position, wage, bonus):
            self.name = name
            self.surname = surname
            self.position = position
            self._income = {"wage": wage, "bonus": bonus}


    class Position(Worker):
        def get_full_name(self):
            return self.name + " " + self.surname

        def get_total_income(self):
            return self._income["wage"] + self._income["bonus"]


    woker_obj = Position("Иван", "Петров", "Банкир", 150000, 25000)
    print(woker_obj.get_full_name())
    print(woker_obj.position)
    print(woker_obj.get_total_income())


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
def lesson_4():
    class Car:
        def __init__(self, speed, color, name, is_police):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_police

        def go(self):
            print(f"{self.name} поехала")

        def stop(self):
            print(f"{self.name} остановилась")

        def turn(self, direction):
            print(f"{self.name} повернула {direction}")

        def show_speed(self):
            print(f"{self.name} - текущая скорость = {self.speed} км/ч")


    class TownCar(Car):
        def show_speed(self):
            Car.show_speed(self)
            max_speed = 60
            if self.speed > max_speed:
                print(f"{self.name} - превышена скорость (больше {max_speed} км/ч)!")


    class SportCar(Car):
        pass


    class WorkCar(Car):
        def show_speed(self):
            Car.show_speed(self)
            max_speed = 40
            if self.speed > max_speed:
                print(f"{self.name} - превышена скорость (больше {max_speed} км/ч)!")


    class PoliceCar(Car):
        pass


    car_obj = Car(50, "зеленый", "обычная машина", False)
    print(car_obj.name, car_obj.speed, car_obj.color, car_obj.is_police)
    car_obj.go()
    car_obj.turn("влево")
    car_obj.show_speed()
    car_obj.stop()

    print()

    towncar_obj = TownCar(70, "красная", "городская машина", False)
    print(towncar_obj.name, towncar_obj.speed, towncar_obj.color, towncar_obj.is_police)
    towncar_obj.go()
    towncar_obj.turn("вправо")
    towncar_obj.show_speed()
    towncar_obj.stop()

    print()

    sportcar_obj = SportCar(30, "синяя", "спортивная машина", False)
    print(sportcar_obj.name, sportcar_obj.speed, sportcar_obj.color, sportcar_obj.is_police)
    sportcar_obj.go()
    sportcar_obj.turn("вправо")
    sportcar_obj.show_speed()
    sportcar_obj.stop()

    print()

    worktcar_obj = WorkCar(80, "желтая", "рабочая машина", False)
    print(worktcar_obj.name, worktcar_obj.speed, worktcar_obj.color, worktcar_obj.is_police)
    worktcar_obj.go()
    worktcar_obj.turn("вправо")
    worktcar_obj.show_speed()
    worktcar_obj.stop()

    print()

    policecar_obj = PoliceCar(100, "белая", "полицейская машина", True)
    print(policecar_obj.name, policecar_obj.speed, policecar_obj.color, policecar_obj.is_police)
    policecar_obj.go()
    policecar_obj.turn("вправо")
    policecar_obj.show_speed()
    policecar_obj.stop()


# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
def lesson_5():
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


if __name__ == "__main__":
    lesson_1()