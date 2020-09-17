from time import sleep, time
import itertools


class TrafficLight:
    __TLcolors = ("Red", "Yellow", "Green")
    # __next_color = iter(__TLcolors)
    __next_color = itertools.cycle(__TLcolors)
    __color = next(__next_color)

    def __change_color(self):
        if self.__color == "Red":
            print(self.__color)
            sleep(7)
        elif self.__color == "Yellow":
            print(self.__color)
            sleep(2)
        elif self.__color == "Green":
            print(self.__color)
            sleep(3)
        else:
            print("err")
        self.__color = next(self.__next_color)

    # было предложение, использовать метод "sleep",
    # моделирования поведения светофора
    def running(self):
        # Светофор будет работать 30 секунд
        time_shutdown = int(time())
        while int(time_shutdown + 30 > time()):
            self.__change_color()
            print(int(time() - time_shutdown))
        print("Работа светофора завершена")


m_svet = TrafficLight()
m_svet.running()

# 1. Создать класс TrafficLight (светофор)
# и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
