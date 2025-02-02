"""
Используйте функцию super()
"""
#super() функция, которая заставит дочерний класс унаследовать все методы
#и свойства от своего родителя

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)       #При использовании super() функции не обязательно использовать имя родительского элемента

x = Student("Mike", "Olsen")
x.printname()