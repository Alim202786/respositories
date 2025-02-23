import re

txt = input("Enter text:")
x = re.sub(r"(?<!^)(?=[A-Z])", "_", txt).lower()
print(x)