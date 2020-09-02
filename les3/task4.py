# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_h(x, y):
    return x ** y


def my_func(x, y):
    if not y:
        return 1
    if not x:
        if y < 0:
            raise ZeroDivisionError('0.0 cannot be raised to a negative power')
        return 0

    temp = x
    for i in range(abs(y) - 1):
        temp *= x
    return temp if y >= 0 else 1/temp


xx, yy = map(int, input("Ввод: ").split())

print(my_func_h(xx, yy))
print(my_func(xx, yy))
