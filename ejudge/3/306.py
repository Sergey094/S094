class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght * self.width

l, w = map(int, input().split())
ar = Rectangle(l, w)
print(ar.area())