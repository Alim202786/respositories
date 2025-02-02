#Удалить свойства объекта
#Вы можете удалить свойства объектов, используя del ключевое слово:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)     #Удалим свойство age из объекта p1:

p1 = Person("John", 36)
del p1.age
print(p1.age)          #из за этого код показывает ошибку