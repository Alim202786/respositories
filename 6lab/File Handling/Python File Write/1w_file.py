"""
Write to an Existing File
"""
#Для записи в существующий файл необходимо добавить параметр в open() функцию
#"a"- Добавить - добавит в конец файла.
#"w"- Запись - перезапишет существующий контент.

#Откройте файл «demofile2.txt» и добавьте в него содержимое
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")        
f.close()

f = open("demofile2.txt", "r")
print(f.read())