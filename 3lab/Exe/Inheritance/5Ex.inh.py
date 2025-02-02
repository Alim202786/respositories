"""
Добавить свойства
"""
#1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019               #Добавьте свойство, вызываемое graduationyear в Studentкласс

x = Student("Mike", "Olsen")
print(x.graduationyear)


#2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year               #Добавьте year параметр и передайте правильный год при создании объектов:

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)