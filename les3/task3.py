# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(ch1, ch2, ch3):
    return sum((ch1, ch2, ch3)) - min(ch1, ch2, ch3)


t1, t2, t3 = map(int, input("Введите 3 целых числа ").split())
print(my_func(t1, t2, t3))
