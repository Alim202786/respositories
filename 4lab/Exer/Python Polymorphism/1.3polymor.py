"""
Inheritance Class Polymorphism
"""
#Если создать Parent class Vehicle и унаследовать от него 
#Car, Boat и Plane, то они получат его методы, но смогут их переопределять.
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

#Child class наследуют свойства и методы родительского класса.
#В примере выше класс Car пустой, но наследует brand, model и move() от Vehicle.
#Классы Boat и Plane также наследуют brand, model и move() от Vehicle, но переопределяют метод move()