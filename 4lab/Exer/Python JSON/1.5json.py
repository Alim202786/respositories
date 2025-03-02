"""
Format the Result
"""
#Вывод JSON-строки неудобен для чтения без отступов и переносов строк.
#Метод json.dumps() поддерживает параметры для удобного форматирования вывода.
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))