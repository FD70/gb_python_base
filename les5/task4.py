endict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}

# One - 1
with open("res/text_4.txt", "r", encoding="utf-8") as input_file:
    with open("created/text_4_out.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            for key in endict:
                line = line.replace(key, endict[key])
            output_file.write(line)

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
