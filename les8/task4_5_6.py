from abc import ABC, abstractmethod


class Storage:
    NONTYPE = "item_null"

    def __init__(self):
        # Можно еще включить проверку на каждый объект, через ввод уникального номера
        # Чтобы нельзя было добавить один и тот же объект на разные/этот же склад
        # Но делать этого здесь я не буду
        self.dict = {
            OfficeEquipment.PRINTER: {},
            OfficeEquipment.SCANNER: {},
            OfficeEquipment.XEROX: {}
        }

    def take_equip(self, equip, count: int = 1):
        """
        Приемка объекта(ов) на склад
            equip -- то, что принимаем
            count -- в каком количестве
        """
        if equip.name in self.dict[equip.get_type()]:
            self.dict[equip.get_type()][equip.name] += count
        else:
            self.dict[equip.get_type()][equip.name] = count

    def get_info(self, item_type=NONTYPE):
        """Вывод всей информации, либо информации по типу техники"""
        if item_type == self.NONTYPE:
            print("Количество техники на складе:")
            for t_type in self.dict:
                temp = 0
                for must_be_number in self.dict[t_type].values():
                    temp += must_be_number
                print(f"{t_type}: {temp}")
        elif item_type not in self.dict:
            print(f"Введен неверный тип техники: {item_type}")
        else:
            print("Вывод по заданному типу техники:")
            for name in self.dict[item_type]:
                print(f"{name:20}: {self.dict[item_type][name]}")


class OfficeEquipment(ABC):
    PRINTER = "item_printer"
    SCANNER = "item_scanner"
    XEROX = "item_xerox"

    @abstractmethod
    def __init__(self, name):
        self.name = name
        self._type = None

    @abstractmethod
    def activate(self):
        pass

    def get_type(self):
        return self._type


class Printer(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)
        self._type = super().PRINTER

    def activate(self):
        self.start_printing()

    def start_printing(self):
        print(f"{self.name} печатает")


class Scanner(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)
        self._type = super().SCANNER

    def activate(self):
        self.start_scanning()

    def start_scanning(self):
        print(f"{self.name} сканирует")


class Xerox(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)
        self._type = super().XEROX

    def activate(self):
        self.start_copy()

    def start_copy(self):
        print(f"{self.name} копирует")


# -------------------------------------------- --------------------------------------------
it_is_my_storage = Storage()

my_own_printer = Printer("Мой любимый принтер")

it_is_my_storage.take_equip(Scanner("Сканер какой-то фирмы"), 12)
it_is_my_storage.take_equip(Scanner("Сканер какой-то фирмы"), 3)
it_is_my_storage.take_equip(Xerox("Ксерк66"), 65)
it_is_my_storage.take_equip(Xerox("Копирайтер 2000"), 23)

# --------------------------------------------
my_own_printer.activate()  # Видите? Мой принтер печатает
it_is_my_storage.take_equip(my_own_printer)

print("-" * 42)
it_is_my_storage.get_info(OfficeEquipment.XEROX)
print("-" * 42)
it_is_my_storage.get_info(OfficeEquipment.SCANNER)
print("~" * 42)
it_is_my_storage.get_info()
print("~" * 42)
it_is_my_storage.get_info("your_wrong_type")
