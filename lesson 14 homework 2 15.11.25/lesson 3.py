class Teacher:
    def __init__(self, name: str, lesson: str):
        self.name = name
        self.lesson = lesson

    def print_info(self):
        print(f"Учитель по {self.lesson} - {self.name}")

teacher1 = Teacher("Михаил", "Программирование")

teacher1.print_info()