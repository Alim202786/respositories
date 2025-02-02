#Функция __str__()
#Функция __str__() контролирует, что должно быть возвращено, когда объект класса представлен в виде строки
#Если __str__() функция не задана, возвращается строковое представление объекта

#1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)            #Строковое представление объекта БЕЗ __str__() функции:
print(p1)


#2
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)             #Строковое представление объекта С __str__() функцией:
print(p1)