prime = lambda n: n > 1 and all(n % i !=0 for i in range(2, int((n)**0.5) + 1))
num = input()
numbers = list(map(int, num.split()))
prime_numbers =list(filter(prime, numbers))
print("Prime numbers: ", prime_numbers)