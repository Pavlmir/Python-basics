# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


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
