def Sphere(R):
    return (4 / 3) * (R)**3 *3.14

R = int(input("Enter radius: "))
print("Volume of a sphere: ",Sphere(R))