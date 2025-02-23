import re

txt = input("Enter text: ")
x = re.findall(r"^a.*b$", txt)

if x:
    print("Match found")
else:
    print("No match")