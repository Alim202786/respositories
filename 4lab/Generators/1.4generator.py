class Squares_Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.current = a  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current > self.b:
            raise StopIteration  
        result = self.current ** 2  
        self.current += 1  
        return result

a = int(input("Enter the start number (a): "))
b = int(input("Enter the end number (b): "))

for square in Squares_Number(a, b):
    print(square)