# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

temp = int(input("время в секундах: "))
# temp = 3599

hours = temp // 3600
mins = (temp % 3600) // 60
sec = temp % 60

if hours < 10:
    hours = "0" + str(hours)
if mins < 10:
    mins = "0" + str(mins)
if sec < 10:
    sec = "0" + str(sec)

print(f"{hours}:{mins}:{sec}")
