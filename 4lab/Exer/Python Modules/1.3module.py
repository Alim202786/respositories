"""
Naming a Module
"""
#Вы можете назвать файл модуля как угодно, но он должен иметь расширение .py

"""
Re-naming a Module
"""
#Вы можете создать псевдоним при импорте модуля, используя as ключевое слово
import second_module as mx

a = mx.person1["age"]
print(a)