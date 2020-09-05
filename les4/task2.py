import random


def get_random_list():
    for el in range(10):
        yield random.randint(1, 100)


random_list = get_random_list()

start_list = []
result = []

temp = next(random_list)
start_list.append(temp)

for i in random_list:
    if temp >= i:
        temp = i
    else:
        temp = i
        result.append(i)
    start_list.append(i)

print(start_list)
print(result)

# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
