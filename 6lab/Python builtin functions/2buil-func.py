def case(s):
    upper_case = sum(1 for char in s if char.isupper())
    lower_case = sum(1 for char in s if char.islower())
    print(f"Uppercase: {upper_case}")
    print(f"Lowercase: {lower_case}")

text = input("Enter case: ")
print(text)
case(text)