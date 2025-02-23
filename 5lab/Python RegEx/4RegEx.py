"""
The split() Function
""" 
#Функция split() возвращает список, в котором строка была разделена при каждом совпадении
import re

txt = "The rain in Spain"
x = re.split(r"\s", txt) 
print(x)

#Вы можете контролировать количество повторений, указав maxsplit параметр
import re

txt = "The rain in Spain"
x = re.split(r"\s", txt, maxsplit=1)  
print(x)
