#Параметр self
#Параметр self является ссылкой на текущий экземпляр класса и используется для доступа к переменным

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):                                #Используйте слова mysillyobject и abc вместо self :
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()