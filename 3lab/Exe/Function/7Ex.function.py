def my_function(country = "Kazakstan"):               #Мы даем country значение поумолчанию
  print("I am from " + country)

#Пример использование
my_function("Sweden")
my_function("India")
my_function()                                         #Здесь по умолчанию будет Kazakstan даже если ничего не писать
my_function("Brazil")