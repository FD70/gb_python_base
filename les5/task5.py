with open("created/text_5.txt", "w", encoding="utf-8") as mfile:
    mfile.write(" ".join(map(str, list(range(1, 11)))))

with open("created/text_5.txt", "r", encoding="utf-8") as mfile:
    string_list = mfile.readline().replace("\n", "").split()
    summm = sum(map(int, string_list))
    print(f"sum: {summm}")

# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
