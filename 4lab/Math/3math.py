import math

n = int(input("Input number of sides:"))
a = float(input("Input the length of a side:"))

S= (n * a **2)/(4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {S:.2f}")