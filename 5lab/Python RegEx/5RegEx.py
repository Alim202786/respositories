"""
The sub() Function
""" 
#Функция sub() заменяет совпадения текстом по вашему выбору
import re

txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)  #Замените каждый пробел на цифру 9
print(x)

#Вы можете контролировать количество замен, указав count параметр
import re

txt = "The rain in Spain"
x = re.sub(r"\s", "0", txt, count=2)
print(x)