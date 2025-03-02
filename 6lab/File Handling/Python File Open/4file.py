"""
Read Lines
"""
#Вы можете вернуть одну строку, используя readline() метод
f = open(f"demofile.txt", "r")
print(f.readline())

print("-------") #не имеет значения

#Позвонив readline() дважды, вы сможете прочитать две первые строки
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

print("-------") #не имеет значения

#Просматривая строки файла, вы можете прочитать весь файл, строка за строкой
f = open("demofile.txt", "r")
for x in f:
  print(x)