class MComplex:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MComplex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        # (x1x2 - y1y2) + (x1y2 + x2y1)i
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + other.x * self.y
        return MComplex(x, y)

    def __str__(self):
        return f"{self.x} {self.y}i"


com1 = MComplex(1, 2)
com2 = MComplex(3, 4)
print(com1 + com2)
print(com1 * com2)

# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
