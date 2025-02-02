class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        
    def area(self):
        return self.lenght * self.width
    
shape = Shape()
print(shape.area())
lenght = int(input("Enter lenght: "))
width = int(input("Enter width: "))
rectangle = Rectangle(lenght, width)
print(rectangle.area())
