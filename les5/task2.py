endict = {
    1: "слово",
    2: "слова",
    3: "слова",
    4: "слова",
}

with open("created/text_1.txt", "r", encoding="utf-8") as mfile:
    for count, line in enumerate(mfile):
        # print(line.replace("\n", ""))
        line = line.replace("\n", "")

        temp_c = len(line.split())
        temp = "слов" if temp_c not in endict else endict[temp_c]

        print(f"{count + 1}: {temp_c} {temp} - {line}")

# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
