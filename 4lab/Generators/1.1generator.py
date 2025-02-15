"""
num = int(input("Enter number: "))

squares = (i ** 2 for i in range(1, num + 1))
for square in squares:
    print(square)
"""

class Square_Number:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

num = int(input("Enter number: "))
squares = Square_Number(num)
for square in squares:
    print(square)