import re

txt = input("Enter text: ")
x = re.findall(r"^[a-z]+_[a-z]+$", txt)

if x:
    print("Match found")
else:
    print("No match")