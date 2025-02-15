"""
The Math Module
"""
#В Python также есть встроенный модуль math, который расширяет список математических функций
#Чтобы использовать его, необходимо импортировать math модуль
#После импорта math модуля вы можете начать использовать методы и константы модуля
#Например, метод math.sqrt() возвращает квадратный корень числа
import math

x = math.sqrt(64)
print(x)

#Метод math.ceil() округляет число вверх, а math.floor() — вниз до ближайшего целого
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#Константа math.pi возвращает значение числа ПИ (3,14...)
import math

x = math.pi
print(x)