"""
Convert from Python to JSON
"""
#Если у вас есть объект Python, вы можете преобразовать его в строку JSON, используя json.dumps() метод
import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)

print(y)