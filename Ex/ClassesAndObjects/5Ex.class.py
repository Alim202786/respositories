#Методы объекта
#Объекты также могут содержать методы. Методы в объектах — это функции, которые принадлежат объекту.Создадим метод в классе Person

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):                                 #Вставьте функцию, которая печатает приветствие, и выполните ее на объекте p1:
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()