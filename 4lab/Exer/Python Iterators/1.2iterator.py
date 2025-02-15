"""
Looping Through an Iterator
"""
#Мы также можем использовать for цикл для итерации итерируемого объекта
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
  #apple
  #banana
  #cherry
                                 #Цикл for фактически создает объект итератора и выполняет next() метод для каждого цикла
#Перебрать символы string
mystr = "banana"

for x in mystr:
  print(x)
  #b
  #a
  #n
  #a
  #n
  #a