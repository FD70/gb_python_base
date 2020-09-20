class MyownExeption(Exception):
    def __init__(self, text="err"):
        self.text = f"MyownException: {text}"


def meth(v1: int, v2: int):
    if v2 == 0:
        raise MyownExeption(f"В выражении {v1}/{v2} присутствует деление на ноль")
    else:
        return v1/v2


try:
    temp = "nothing"
    temp = meth(1, 0)
except MyownExeption as e:
    print(e.text)
finally:
    print(temp)

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
