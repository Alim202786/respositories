def Palindrome(word):
    cleaned_string = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

word = input("Enter word: ")
print(Palindrome(word))  
