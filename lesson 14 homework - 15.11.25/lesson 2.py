class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def print_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}")

my_person = Person("Mikhail", 18, "Almaty")
my_person.print_info()