"""
Check if NOT
"""
#Чтобы проверить, присутствует ли определенная фраза или символ в строке, 
# мы можем использовать ключевое слово not in

#1
txt = "The best things in life are free!"
print("expensive" not in txt)

#2
txt = "The best things in life are free!"
if "expensive" not in txt:                    #Используйте его в if утверждении
  print("No, 'expensive' is NOT present.")