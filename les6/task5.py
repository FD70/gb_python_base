class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Уникальный метод для {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} начинает рисовать")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} не пишет")


st1 = Pen("Карандаш из магазина")
st2 = Pencil("Ручка соседа")
st3 = Handle("Нашел маркер,")

st1.draw()
st2.draw()
st3.draw()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
