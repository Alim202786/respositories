"""
Order the Result
"""
#Метод json.dumps() имеет параметры для упорядочивания ключей в результате
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

print(json.dumps(x, indent=4, sort_keys=True))   #Используйте sort_keys параметр, чтобы указать, следует ли сортировать результат