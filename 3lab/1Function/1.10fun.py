def Unique(number):
    unique_list = []
    for num in number:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

number = list(map(int, input("Enter number: ").split()))
print(Unique(number))