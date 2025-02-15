"""
Function Polymorphism
"""
#Пример универсальной функции в Python — len(), которая работает с разными объектами

#String
x = "Hello World!"

print(len(x))  #Для строк len()возвращает количество символов

#Tuple
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))  #Для кортежей len()возвращает количество элементов в tuple

#Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))  #Для словарей len()возвращает количество пар ключ/значение в dictionary