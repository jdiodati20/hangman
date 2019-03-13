class shape:
    def what_am_i(self):
        print("I am a shape")

class square(shape):
    square_list = []
    def __init__(self, side):
        self.side = side
        self.square_list.append(self)
    def __repr__(self):
        return("{} by {} by {} by {}".format(self.side, self.side, self.side, self.side))
    def __what__(self):
        return("whoa")

def equals(object1, object2):
    return(object1 is object2)

length = input("How long do you want each side of the square to be? \n")
a = square(length)
print(a)
g = "a"
c = "a"
print(equals(c, g))
