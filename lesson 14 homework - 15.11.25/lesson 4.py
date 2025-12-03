class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} издает звук")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} лает")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} мяукает")

my_animal = Animal("Бобик", 36)
my_animal.speak()

my_dog = Dog("Шарик", 50)
my_dog.speak()

my_cat = Cat("Мурка", 2)
my_cat.speak()