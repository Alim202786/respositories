import re

txt = input("Enter text: ")
x = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), txt)
print(x)