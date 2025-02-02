import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    random_number = random.randint(1, 20)
    count = 0
    
    while True:
        print("Take a guess.")
        number = int(input())
        count += 1
        if number > random_number:
            print("Your guess is too low")
        elif number < random_number:
            print("Your guess is too low")
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break
            
guess_the_number()