"""
The search() Function
""" 
#Функция search() ищет совпадение в строке и возвращает объект Match , если совпадение есть
#Если совпадений несколько, будет возвращено только первое совпадение
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#None Если совпадений не найдено, возвращается значение
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)