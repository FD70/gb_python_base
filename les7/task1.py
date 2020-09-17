class MyMatrix(object):
    def __init__(self, *args):
        # размерность матрицы
        self.__n = len(args[0])
        self.__m = len(args)
        # заполнение
        self.__content = []
        for line in args:
            if len(line) == self.__n:
                self.__content.append(line)
            else:
                raise ValueError("MyMatrix - некорректно объявлена матрица")

    def __add__(self, other):
        # проверка размерностей
        if self.__n == other.__n and self.__m == other.__m:
            # сложение
            temp_content = []
            for i in range(self.__n):
                temp_line = []
                for j in range(self.__m):
                    summ = self.get_element(i, j) + other.get_element(i, j)
                    temp_line.append(summ)
                temp_content.append(temp_line)
            # return MyMatrix(el for el in temp_content)
            return MyMatrix(*temp_content)
        else:
            raise ValueError("Нельзя сложить матрицы разных размерностей!")

    def __str__(self):
        temp_str = ""
        for line in self.__content:
            temp_str = f"{temp_str}\n{line}"
        return temp_str

    def get_element(self, m: int, n: int):
        return self.__content[int(m)][int(n)]


my_matrix1 = MyMatrix([1, 2],
                      [3, 4])

my_matrix2 = MyMatrix([-3, 2.2],
                      [-10, 50])

my_matrix3 = my_matrix1 + my_matrix2
print(my_matrix3)
