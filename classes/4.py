class Point():
    def __init__(self, x, y):  
        self.x = x
        self.y = y    

    def show(self):
        cor = input()
    
    def move(self):
        change = input()

    def dist(px1, px2):
        return ((px1-px2)**2+(py1-py2)**2)**0.5

px1 = Point(5, 5)
px2 = Point(2, 3)
print(dist(px1, px2))