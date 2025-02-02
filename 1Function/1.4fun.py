def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if prime(n)]  

number = list(map(int, input("Enter numbers: ").split()))
number_prime = filter_prime(number)
print("Prime numbers", number_prime)
