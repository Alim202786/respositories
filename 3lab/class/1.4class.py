class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def dist(self,other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)**0.5
    
x1 = int(input("Enter x for point1: "))
y1 = int(input("Enter y for point1: "))
point1 = Point(x1, y1)

x2 = int(input("Enter x for point2: "))
y2 = int(input("Enter y for point2: "))
point2 = Point(x2, y2)

#1
#метод showотображения координат точки
print("coordinates of point1: ")
point1.show()
print("coordinates of point2: ")
point2.show()

#2
#метод moveизменения этих координат
dx1 = int(input("Enter move point1 on the x-axis: "))
dy1 = int(input("Enter move point1 on the y-axis: "))
point1.move(dx1, dy1)

dx2 = int(input("Enter move point2 on the x-axis: "))
dy2 = int(input("Enter move point2 on the y-axis: "))
point2.move(dx2, dy2)

print("New coordinates of point1: ")
point1.show()
print("New coordinates of point2: ")
point2.show()

#3
#метод dist, который вычисляет расстояние между 2 точками
distance = point1.dist(point2)
print(f"Distance point1 and point2: {distance}")