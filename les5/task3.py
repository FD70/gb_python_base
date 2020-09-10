# Иванов 10000.0
with open("res/text_3.txt", "r", encoding="utf-8") as mfile:
    total = 0

    for count, line in enumerate(mfile):
        temp_c = float(line.split()[1])
        total += temp_c
        if temp_c < 20000.0:
            # print(line.split()[0])
            print(line.replace("\n", ""))

    print(f"\naverage: {total/(count + 1)}")

# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
