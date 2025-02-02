#Изменить свойства объекта
#Вы можете изменять свойства объектов следующим образом

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)      #Установите возраст p1 равным 40:

p1 = Person("John", 36)
p1.age = 40
print(p1.age)
