# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def is_digit(val):
    """Проверка на число"""
    try:
        float(val)
        return True
    except ValueError:
        return False


all_sum = 0
while True:
    input_list = list(input("Введите числа через пробел, выход - любой нечисловой символ ").split())

    temp_sum = 0
    flag = False
    for i in input_list:
        if is_digit(i):
            temp_sum += float(i)
        else:
            flag = True
            break

    all_sum += temp_sum
    print(f"Сумма текущего ввода: {temp_sum}\nВся сумма: {all_sum}")
    print("-" * 42)
    if flag:
        break
