"""
Local Scope
"""
#Переменная, созданная внутри функции, принадлежит Local Scope действия этой функции и может использоваться только внутри этой функции.
def myfunc():
  x = 300
  print(x)

myfunc()     #Переменная, созданная внутри функции, доступна внутри этой функции