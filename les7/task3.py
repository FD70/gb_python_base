class Cells:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return Cells(self.count + other.count)

    def __sub__(self, other):
        temp = self.count - other.count
        if temp < 0:
            raise ValueError("Отрицательное значение")
        else:
            return Cells(temp)

    def __mul__(self, other):
        return Cells(self.count * other.count)

    def __truediv__(self, other):
        return Cells(self.count // other.count)

    def __str__(self):
        return f"Клеток - {self.count}"

    def make_order(self, line_value, syms: str = "#") -> str:
        temp = (self.count // line_value) * (syms * line_value + "\n")
        temp += (self.count % line_value) * syms
        return temp


print(Cells(1) + Cells(2))
print(Cells(3) - Cells(2))
print(Cells(5) / Cells(3))
print(Cells(2) * Cells(9))
print("-" * 33)

print(Cells(6).make_order(4))
print(Cells(7).make_order(2, "_/"))
