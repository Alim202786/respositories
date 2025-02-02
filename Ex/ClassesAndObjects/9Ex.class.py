#Удалить объекты
#Вы можете удалить объекты, используя del ключевое слово

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)     #Удалить объект p1:

p1 = Person("John", 36)
del p1
print(p1)       #из за этого код показывает ошибку