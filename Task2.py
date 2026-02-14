class BankAccount:
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("New Balance:", self.balance)
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.balance)


# Example usage
account1 = BankAccount("John", 1000)

account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)
