"""
Создать родительский класс
"""
#Любой класс может быть родительским классом,
#поэтому синтаксис такой же, как и при создании любого другого класса

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):                           #Создайте класс с именем Person, со firstname свойствами lastnameи printname методом
    print(self.firstname, self.lastname)

#Используйте класс Person для создания объекта, а затем выполните метод printname

x = Person("John", "Doe")
x.printname()