import re

txt = input("Enter text:")
x = re.split(r'(?=[A-Z])', txt)
print(x)