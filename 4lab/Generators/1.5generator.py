class Count_down:
    def __init__(self, n):
        self.n = n  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.n < 0:
            raise StopIteration  
        result = self.n  
        self.n -= 1  
        return result

n = int(input("Enter a number: "))

for num in Count_down(n):
    print(num)