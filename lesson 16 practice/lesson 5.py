import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1.distance(p2))

p1.move(2, 3)
print(p1.distance(p2))