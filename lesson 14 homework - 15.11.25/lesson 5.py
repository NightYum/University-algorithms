class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return 0.5 * self.a * self.b

def print_area(shape):
    print(shape.area())

figures = [
    Circle(3),
    Square(3),
    Triangle(4, 5)
]

for fig in figures:
    print_area(fig)