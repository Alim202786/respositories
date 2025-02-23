import re

txt = input("Enter text: ")
x = re.findall(r"^ab{2,3}$", txt)

if x:
    print("Match found")
else:
    print("No match")