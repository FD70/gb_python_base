#  Для списка реализовать обмен значений соседних элементов,
#  т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#  При нечетном количестве элементов последний сохранить на своем месте.
#  Для заполнения списка элементов необходимо использовать функцию input().

my_list = []

while True:
    print("Введите новое значение, для выхода введите '0'")
    temp = input("Новое значение: ")
    if temp == "0":
        break
    else:
        my_list.append(temp)
        print(f"Введено значение: {temp}")
        print("Вот весь список:")
        print(my_list)
        print("*" * 42 + "\n")

# Заполнили список, затем делаем замену
for i in range(1, len(my_list), 2):
    # swap
    # fortemp = my_list[i]
    # my_list[i] = my_list[i-1]
    # my_list[i-1] = fortemp

    my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
    # print(my_list[i])
print("Список после всех замен:")
print(my_list)
