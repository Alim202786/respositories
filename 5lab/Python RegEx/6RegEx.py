"""
Match Object
""" 
#A Match Object — это объект, содержащий информацию о поиске и результате.
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)                  #<re.Match object; span=(5, 7), match='ai'>

#.span() возвращает кортеж, содержащий начальную и конечную позиции совпадения
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())            #(12, 17)

#.string возвращает строку, переданную в функцию
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)             #The rain in Spain

#.group() возвращает часть строки, где было совпадение
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())             #Spain
