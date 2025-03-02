import math
import time

number = int(input("Enter number: "))
delay = int(input("Enter delay is milliseconds: "))
result = math.sqrt(number)
time.sleep(delay / 1000)
print(F"Square root of {number} after {delay} miliseconds is {result}")