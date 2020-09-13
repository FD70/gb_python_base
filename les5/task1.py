with open("created/text_1.txt", "w", encoding="utf-8") as mfile:
    print("type 'q' for exit")
    while True:
        temp = input("Записать: ")
        if temp == 'q':
            break
        else:
            mfile.write(temp + "\n")

# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
