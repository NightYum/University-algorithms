class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_info(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет, моя оценка {self.grade}")

mikhail = Student("Михаил", 18, 100)
mikhail.print_info()