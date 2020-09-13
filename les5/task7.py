import json

comps = {}
av_prof = {}
output_list = [comps, av_prof]

# Brooms ПАО 2500000 500000
with open("res/text_7.txt", "r", encoding="utf-8") as mfile:
    # Вся прибыль неубыточных компаний, их количество
    total_suc_prof = 0
    tsc_count = 0

    for line in mfile:
        name, mtype, f_plus, f_minus = line.split()
        f_plus = int(f_plus)
        f_minus = int(f_minus)

        comps[name] = f_plus - f_minus
        if f_plus > f_minus:
            tsc_count += 1
            total_suc_prof += f_plus - f_minus

    av_prof["average_profit"] = total_suc_prof / tsc_count

with open("created/text_7_out.json", "w", encoding="utf-8") as output_file:
    json.dump(output_list, output_file, ensure_ascii=False, indent=4)

# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджеры контекста.
