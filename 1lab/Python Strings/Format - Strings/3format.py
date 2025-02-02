"""
Placeholders and Modifiers
"""
#Placeholders может содержать переменные, 
#операции, функции и Modifiers для форматирования значения
#1
price = 59
txt = f"The price is {price} dollars"
print(txt)


#2
price = 59
txt = f"The price is {price:.2f} dollars"    #Отобразить цену с двумя знаками после запятой
print(txt)


#3
txt = f"The price is {20 * 59} dollars"     #Заполнитель может содержать код Python, например, математические операции
print(txt)