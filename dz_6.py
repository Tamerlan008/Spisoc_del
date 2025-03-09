class SpisokDel:
    def __init__(self):
        self.spisok_del = []

    def d(self):
        while True:
            l = input("Введите задачу или 'выход' для завершения: ")
            if l.lower() == 'выход':
                break
            self.spisok_del.append(l)

    def d2(self):
        if self.spisok_del:
            print("Ваши задачи:")
            for i, l in enumerate(self.spisok_del, start=1):
                print(f"{i}. {l}")
        else:
            print("Список дел пуст")

    def s(self):
        print("Добро пожаловать в 'Список дел'")
        self.d()
        self.d2()


приложение = SpisokDel()
приложение.s()

