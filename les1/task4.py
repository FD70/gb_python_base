# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
# number = 12761285

max_of = 0

while True:
    if number > 10:
        temp = number % 10
        number = number // 10
        if max_of < temp:
            max_of = temp
    else:
        break

print(f"Максимальная цифра {max_of}")
