def reverse():
    sentence = input("Enter string: ")
    words = sentence.split()  
    reversed_words = ' '.join(reversed(words))  
    return reversed_words

result = reverse()
print(result)