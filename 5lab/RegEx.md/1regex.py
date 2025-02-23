import re

txt = input("Enter text: ")
x = re.findall(r"^ab*$", txt)

if x:
    print("Match found")
else:
    print("No match")