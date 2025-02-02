class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
            self.balance += amount
            print(f"{amount} deposit. New balance {self.balance}")
            
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} remove. New balance {self.balance}")
        else:
            print("Insufficient funds for withdraw")
            
name = input("Owner: ")
balance = int(input("Account balance: "))
account = Account(name, balance)

while True:
    action = input("What do you want to do? (deposit/withdraw): ")
    if action == 'deposit':
        amount = int(input("Enter deposit: "))
        account.deposit(amount)
        break
    elif action == 'withdraw':
        amount = int(input("Enter withdraw: "))
        account.withdraw(amount)
        break
    else:
        print("Error")
        break