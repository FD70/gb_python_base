import random
# Направления
DIRS = ("Лево", "Право", "Назад")


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
        print(f"Текущаяя скорость {self.name} - {self.speed}")


class TownCar(Car):
    _speed_limit = 60

    def show_speed(self):
        print(f"Текущаяя скорость {self.name} - {self.speed}")
        if self.speed > self._speed_limit:
            print(f"Превышение скорости для {self.name}")


class SportCar(Car):
    pass


class WorkCar(Car):
    _speed_limit = 40

    def show_speed(self):
        print(f"Текущаяя скорость {self.name} - {self.speed}")
        if self.speed > self._speed_limit:
            print(f"Превышение скорости для {self.name}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, car):
        super().__init__(speed, color, name, is_police)
        self.purpose = car

    def go(self):
        print(f"{self.name} выдвинулся за {self.purpose.name}")


work1 = WorkCar(42, "Белый", "Грузовик", False)
work2 = WorkCar(30, "Синий", "Камаз", False)

work1.go()
work2.go()

work2.show_speed()
work1.show_speed()

police1 = PoliceCar(120, "Черный", "PoliceCar1", True, work1)
police1.go()

work1.turn(random.choice(DIRS))
police1.turn(random.choice(DIRS))

# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
