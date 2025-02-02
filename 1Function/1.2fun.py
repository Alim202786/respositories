def fahrenheit_celsius(F):
    return (5 / 9) * (F - 32)

F = float(input("F: "))
C = fahrenheit_celsius(F)
print(f"{F} is equal {C:.2f}")