def grams_ounces(grams):
    return 28.3495231 * grams
grams = float(input("grams: "))
ounces = grams_ounces(grams)
print(f"{grams} is equal to {ounces:.2f}")