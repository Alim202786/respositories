"""
Parse JSON - Convert from JSON to Python
"""
#Если у вас есть строка JSON, вы можете проанализировать ее с помощью json.loads() метода
import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y["age"])