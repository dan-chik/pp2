class Shape():
    def __init__(self):
        pass

    def Area(self, length = 0):
        return self.length*self.length


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def Area(self, length = 0):
        return self.length*self.length

x = Square(5)
print(x.Area())

