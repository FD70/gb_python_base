# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

text = input("Опишите себя: ")

list = text.split()

print("Вы утверждаете, что: ")
for i in range(len(list)):
    print(f"{i}. {list[i][:10]}")
