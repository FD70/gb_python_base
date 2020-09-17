from abc import ABC, abstractmethod


class Cloth(ABC):
    __outlay = 0

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def append_outlay(self, value: float):
        Cloth.__outlay += value

    # Я сейчас без понятия, как организовать здесь без self=None
    def get_outlay(self=None):
        return f"Общий расход ткани {Cloth.__outlay:.3f}"


class Coat(Cloth):  # Пальто
    # Общий расход
    _coat_outlay = 0

    def __init__(self, name, size: float):
        super().__init__(name)
        self.size = size
        # для пальто (V/6.5 + 0.5)
        self.outlay = (size / 6.5 + 0.5)
        Coat._coat_outlay += self.outlay
        super().append_outlay(self.outlay)

    @property
    def outlay(self):
        return self.__outlay

    @outlay.setter
    def outlay(self, value):
        self.__outlay = value

    def __str__(self):
        return f"{self.name} - расход: {self.outlay:.3f}"


class Suit(Cloth):  # Костюм
    _suit_outlay = 0

    def __init__(self, name, height: int):
        super().__init__(name)
        self.height = height
        # для костюма (2 * H + 0.3)
        self.outlay = (2 * height + 0.3)
        Suit._suit_outlay += self.outlay
        super().append_outlay(self.outlay)

    @property
    def outlay(self):
        return self.__outlay

    @outlay.setter
    def outlay(self, value):
        self.__outlay = value

    def __str__(self):
        return f"{self.name} - расход: {self.outlay:.3f}"


ss = Suit("Костюм", 21)
ss2 = Suit("Кост", 12)
print(ss)
print(ss2)

cc = Coat("Пальто", 42.2)
print(cc)

print(Cloth.get_outlay())

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
