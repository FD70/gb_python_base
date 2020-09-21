class MclassDate:
    """Take 'dd-mm-yyyy'"""
    def __init__(self, string_date: str):
        self.__raw = string_date
        self.date = self.extract(self.__raw)

    @classmethod
    def extract(cls, raw_str):
        if cls.validation(raw_str)[0]:
            return tuple(map(int, raw_str.split("-")))
        else:
            return cls.extract("01-01-0001")

    @staticmethod
    def validation(str_date: str):
        """ :returns bool, message(if smth, wrong)

        ! Не учитывалось, что в разных месяцах, разное количество дней !
        """
        # message = "#"
        temp = str_date.split("-")
        try:
            day = int(temp[0])
            month = int(temp[1])
            year = int(temp[2])
        except (ValueError, IndexError):
            # print(e.__class__)
            message = f"Неверный формат ввода 'dd-mm-yyyy' для '{str_date}'"
            return False, message
        else:
            if not 0 < day < 32:
                message = f"Неверно введена дата: {day}, для {str_date}"
                return False, message
            if not 0 < month < 13:
                message = f"Неверно введен месяц: {month}, для {str_date}"
                return False, message
            if not 0 <= year < 3000:
                message = f"Вероятно, неверно введен год {year}, для {str_date}"
                return False, message
        return True, str_date

    def __str__(self):
        return f"{self.date[0]:0=2}-{self.date[1]:0=2}-{self.date[2]:0=4}"
        # return f"{'-'.join(map(str, self.date))}"


new_date = MclassDate("20-09-2020")
wrong_date = MclassDate("32-13-2077")
print(new_date)
print(wrong_date)

print(MclassDate.validation("01-01-1993"))
print(MclassDate.validation("1-asdf1-1"))
print(MclassDate.validation("32-13-2077"))


# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
