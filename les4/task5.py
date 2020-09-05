import random
import functools


random_list = [random.randrange(100, 1000) for i in range(2)]
print(random_list)

print(functools.reduce(lambda x, y: x * y, random_list))

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
