"""
Создать дочерний класс
"""
#Создайте класс с именем Student, который будет наследовать свойства и методы от Person класса

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):                #Создайте класс с именем Student, который будет наследовать свойства и методы от Person класса
  pass                                #используйте pass ключевое слово, если вы не хотите добавлять в класс какие-либо другие свойства

x = Student("Mike", "Olsen")
x.printname()                         #Используйте Student класс для создания объекта, а затем выполните printname метод
