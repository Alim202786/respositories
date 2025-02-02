class string_text:
    def __init__(self):
        self.text = ""
    def getString(self):
        self.text = input("Enter string: ")
    def printString(self):
        print(self.text.upper())
        
obj = string_text()
obj.getString()
obj.printString()