"""
Глобальные переменные
"""
#Переменные, которые создаются вне функции называются глобальными переменными.

#1
x = "awesome"

def myfunc():
  print("Python is " + x)        #Создайте переменную вне функции и используйте ее внутри функции.

myfunc()


#2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
