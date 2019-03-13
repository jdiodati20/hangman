import math

#parent classes
class shape():
    def what_am_i(self):
        print("I am a shape")

#child classes
class rectangle(shape):
    def __init__(self, length, width):
        self.l = length
        self.w = width
    def area(self):
        return self.l * self.w

class square(shape):
    def __init__(self, sideLength):
        self.side = sideLength
    def area(self):
        return self.side ** 2
    def change_size(self, difference):
        self.side -= difference

class horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class rider:
    def __init__(self, name):
        self.name = name

r = rectangle(2, 3)
s = square(4)
rArea = r.area()
sArea = s.area()
print(rArea)
print(sArea)

s.change_size(1)
sArea = s.area()
print(sArea)

s.what_am_i()
r.what_am_i()

person = rider("max")
horse = horse("jack", person)
print(horse.rider.name)
