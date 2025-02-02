def permute(x, y, z):
    if y == z:
        print("".join(x))
    else:
        for i in range(y, z):
            x[y], x[i] = x[i], x[y]  
            permute(x, y + 1, z) 
            x[y], x[i] = x[i], x[y]  

def print_permutations(string):
    x = list(string)  
    permute(x, 0, len(x))

str = input("Enter a string: ")
print_permutations(str)
