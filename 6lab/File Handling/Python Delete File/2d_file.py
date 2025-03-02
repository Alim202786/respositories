"""
Check if File exist
"""
#Чтобы избежать ошибки, перед попыткой удаления файла проверьте, существует ли он

import os
if os.path.exists("demofile.txt"):   #Проверьте, существует ли файл, затем удалите его
  os.remove("demofile.txt")
else:
  print("The file does not exist")