"""
Naming Variables
"""
#Если в функции используется переменная с тем же именем,
#что и вне её, Python рассматривает их как две разные переменные: 
#Global Scope (вне функции), а другая Local Scope (внутри функции)
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()   #200
print(x)   #300