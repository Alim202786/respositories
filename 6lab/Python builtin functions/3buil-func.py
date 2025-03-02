def palindrome(s):
    s = s.lower()
    return s == s[::-1]

text = input("Enter string: ")
if palindrome(text):
    print("Yes is palindrome")
else:
    print("No is not palindrome")