# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

input_month = int(input("Введите месяц от 1 до 12: "))

WINTER = (12, 1, 2)
SPRING = (3, 4, 5)
SUMMER = (6, 7, 8)
AUTUMN = (9, 10, 11)

m_list = ["зима", "весна", "лето", "осень"]
if input_month in WINTER:
    print(m_list[0])
elif input_month in SPRING:
    print(m_list[1])
elif input_month in SUMMER:
    print(m_list[2])
elif input_month in AUTUMN:
    print(m_list[3])


# m_dict = {"_1_2_12": "зима", "_3_4_5": "весна", "_6_7_8": "лето", "_9_10_11": "осень"}
m_dict = {WINTER: "зима",
          SPRING: "весна",
          SUMMER: "лето",
          AUTUMN: "осень"}

for i in m_dict:
    if input_month in i:
        print(m_dict[i])
