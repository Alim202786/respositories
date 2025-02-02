def my_function(**kid):                                 #Если не знаешь сколько ключевых аргументов будет используй ( ** )
  print("His last name is " + kid["lname"])             

#Пример использование
my_function(fname = "Marat", lname = "Dim")