"""
The findall() Function
"""
#Функция findall() возвращает список, содержащий все совпадения
import re

txt = "The rain in Spain"
x = re.findall("n", txt)
print(x)
#Список содержит совпадения в порядке их нахождения.

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)        
print(x)                           #Если совпадений не найдено, возвращается пустой список

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")