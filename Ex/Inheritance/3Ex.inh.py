"""
Добавьте функцию __init__()
"""
#функция __init__()вызывается автоматически каждый раз,
#когда класс используется для создания нового объекта

class Person:
  def __init__(self, fname, lname):           #Добавьте __init__() функцию в Student класс:
    self.firstname = fname                    #__init__() Функция потомка переопределяет наследование функции родителя __init__()
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
