import itertools
import random

m_list = []
t_list = []

for i in itertools.count(97):
    m_list.append(random.randint(i, 122))
    if len(m_list) > 5:
        print(m_list)
        break

for j in itertools.cycle(m_list):
    t_list.append(chr(j))
    if len(t_list) > 2 * len(m_list):
        print(t_list)
        break

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
