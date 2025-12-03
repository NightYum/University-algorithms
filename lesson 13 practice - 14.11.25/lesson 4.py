class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_p(self):
        return self.width * 2 + self.height * 2

    def get_s(self):
        return self.width * self.height

r1 = Rectangle(100, 100)
r2 = Rectangle(20, 20)

print(r1.get_p(), r1.get_s())
print(r2.get_p(), r2.get_s())

print(r1.get_s() if r1.get_s() > r2.get_s() else r2.get_s())