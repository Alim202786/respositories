#Функция __init__()
#Создайте класс с именем Person, используйте __init__() функцию для назначения значений имени и возраста
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Adil", 9)

print(p1.name)
print(p1.age)