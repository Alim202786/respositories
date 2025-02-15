"""
StopIteration
"""
#Прошлый пример работал бы бесконечно при достаточном количестве вызовов next() или в for-цикле.
#Чтобы избежать бесконечного цикла, используйте StopIteration.
#В __next__() добавляем условие, вызывающее StopIteration после указанного числа итераций.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1               #Остановка после 20 итераций
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)