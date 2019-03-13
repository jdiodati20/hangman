import math

class apple:
    def __init__(self, color, size, shape, weight):
        self.c = color
        self.s = size
        self.sh = shape
        self.w = weight
class circle:
    def __init__(self, radius):
        self.r = radius
    def area(self):
        return math.pi * self.r * self.r

class triangle:
    def __init__(self, base, height):
        self.b = base
        self.h = height
    def area(self):
        return self.b * self.h * 0.5

class hexagon:
    def __init__(self, sideLength):
        self.l = sideLength
    def calculate_perimeter(self):
        return 6 * self.l

cir = circle(1)
a = cir.area()
print(a)

tri = triangle(3, 4)
a1 = tri.area()
print(a1)

hexa = hexagon(6)
a2 = hexa.calculate_perimeter()
print(a2)
