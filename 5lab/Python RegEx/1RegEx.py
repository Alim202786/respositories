"""
RegEx in Python
"""
#Python имеет встроенный модуль re для работы с регулярными выражениями.
#После импорта reмодуля вы можете начать использовать регулярные выражения
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  #Найдите строку, чтобы увидеть, начинается ли она с «The» и заканчивается ли на «Spain»

if x:
  print("YES! We have a match!")
else:
  print("No match")