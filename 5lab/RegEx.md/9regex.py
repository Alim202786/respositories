import re

txt = input("Enter text:")
x = re.sub(r"(?=[A-Z])", " ", txt)
print(x)