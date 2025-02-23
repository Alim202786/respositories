import re

txt = input("Enter text: ")
x = re.sub(r"[ ,.]", ":", txt)
print(x)