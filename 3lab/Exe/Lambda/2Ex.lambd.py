def myfunc(n):                    #функции
  return lambda a : a * n         #умножен на неизвестное число

#1
mydoubler = myfunc(2)             #Используйте это  функции, чтобы создать функцию, которая всегда удваивает
print(mydoubler(11))


#2
mydoubler = myfunc(2)             #Используйте это  функции, чтобы создать функцию, которая всегда утраивает
print(mydoubler(11))