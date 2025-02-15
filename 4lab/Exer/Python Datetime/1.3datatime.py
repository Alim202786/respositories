"""
The strftime() Method
"""
#Объект datetime имеет метод для форматирования объектов даты в читаемые строки
#Метод называется strftime()и принимает один параметр, format, для указания формата возвращаемой строки
import datetime

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))