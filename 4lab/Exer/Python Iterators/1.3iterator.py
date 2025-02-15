"""
Create an Iterator
"""
#Чтобы создать object/class как итератор, реализуйте __iter__() и __next__()
#__iter__() может выполнять операции __init__()(инициализацию и т. д.), но должен возвращать сам итератор.
#__next__() выполняет операции и возвращает следующий элемент.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))  #1
print(next(myiter))  #2
print(next(myiter))  #3
print(next(myiter))  #4
print(next(myiter))  #5