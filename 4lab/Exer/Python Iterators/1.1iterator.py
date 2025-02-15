"""
Iterator vs Iterable
"""
#List, tuple, dictionaries и sets — все это итерируемые объекты.
#Это итерируемые контейнеры , из которых можно получить итератор.

#Все эти объекты имеют iter() метод, который используется для получения итератора

#Верните итератор из tuple и выведите каждое значение
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  #apple
print(next(myit))  #banana
print(next(myit))  #cherry   


#String также являются итерируемыми объектами, содержащими последовательность символов
mystr = "banana"
myit = iter(mystr)

print(next(myit))  #b
print(next(myit))  #a
print(next(myit))  #n
print(next(myit))  #a
print(next(myit))  #n
print(next(myit))  #a