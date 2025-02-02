class Shape:
    def area(self):
        return 0

class Squar(Shape):
    def __init__(self, lenght):
        self.lenght = lenght
        
    def area(self):
        return self.lenght * self.lenght
    
shape = Shape()
print(shape.area())
lenght = int(input("Enter lenght: "))
squar = Squar(lenght)
print(squar.area())