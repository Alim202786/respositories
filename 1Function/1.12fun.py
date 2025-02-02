def histogram(number):
    for num in number: 
        print('*' * num)
            
number = list(map(int, input("Enter number: ").split()))
histogram(number)