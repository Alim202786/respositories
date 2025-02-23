import re

txt = input("Enter text: ")
x = re.findall(r"[A-Z]+[a-z]", txt)

if x:
    print("Match found")
else:
    print("No match")