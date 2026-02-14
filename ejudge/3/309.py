class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        pi = 3.14159
        answer = self.radius * self.radius * pi 
        print(f"{answer:.2f}")

rad = int(input())
ar = Circle(rad)
ar.area()