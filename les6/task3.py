MANAGER = "Менеджер"
DIRECTOR = "Директор"


class Worker:
    # должность: оклад, премия
    denezki = {
        MANAGER: (1000, 222),
        DIRECTOR: (2000, 111)
    }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.denezki[position]


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return f"Имя: {self.surname} {self.name} : {self.position}"

    def get_total_income(self):
        temp = self._income[0] + self._income[1]
        return f"ЗП: {temp} ( Оклад: {self._income[0]} Премия: {self._income[1]} )"


wrk_1 = Position("Антон", "Петров", MANAGER)
wrk_2 = Position("Анна", "Барышнева", DIRECTOR)

print(wrk_1.get_full_name())
print(wrk_1.get_total_income())

print(wrk_2.get_full_name())
print(wrk_2.get_total_income())

# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
