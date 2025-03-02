def all_elements_true(tup):
    return all(tup)

user_input = input("Enter True/False: ").split()
tuple = tuple(map(lambda x: x.lower() == 'true', user_input)) 

print(all_elements_true(tuple))