"""
Python Dates
"""
#В Python дата — не отдельный тип данных, но с ней можно работать через модуль datetime
import datetime

x = datetime.datetime.now()
print(x)


#Верните год и название дня недели
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))