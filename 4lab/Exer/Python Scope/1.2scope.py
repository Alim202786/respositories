"""
Function Inside Function
"""
#Как поясняется в примере выше, переменная xнедоступна вне функции, но доступна для любой функции внутри функции
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()    #Доступ к локальной переменной можно получить из функции внутри функции