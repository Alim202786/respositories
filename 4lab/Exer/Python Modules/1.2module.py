"""
Variables in Module
"""
#Модуль может содержать функции, как уже было описано, а также переменные всех типов
#Такие как arrays, dictionaries, objects и т.д
#Создаем файле с именем second_module.py и сохраняем код

"""
Use a Module
"""
#Импортируйте модуль с именем second_module и получите доступ к словарю person1
import second_module

a = second_module.person1["age"]
print(a)