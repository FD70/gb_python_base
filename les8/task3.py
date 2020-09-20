class ListCheckerWithEx(Exception):
    __output = []

    def __init__(self, text="err"):
        self.text = f"MyownException: {text}"

    @staticmethod
    def check_this(value):
        try:
            value = float(value)
            # Если нет ошибки - value число
            ListCheckerWithEx.__output.append(value)
        except ValueError:
            raise ListCheckerWithEx(f"Ошибка - '{value}' не число")

    @staticmethod
    def mainloop():
        print("Введите числа, для выхода введите 'q'")
        while True:
            try:
                temp = input("Следующее значение: ")
                if not temp.lower() == "q":
                    ListCheckerWithEx.check_this(temp)
                else:
                    break
            except ListCheckerWithEx as e:
                print(e.text)

    @classmethod
    def get_list(cls):
        return cls.__output


ListCheckerWithEx.mainloop()
print(ListCheckerWithEx.get_list())
