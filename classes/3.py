class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rec_area(self):
        return self.length*self.width

x = Rectangle(11, 7)
print(x.rec_area())