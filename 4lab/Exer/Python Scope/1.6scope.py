"""
Nonlocal Keyword
"""
#Ключевое nonlocal слово используется для работы с переменными внутри вложенных функций.
#Ключевое nonlocal слово делает переменную принадлежащей внешней функции.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())