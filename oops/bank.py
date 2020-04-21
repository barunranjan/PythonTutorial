import sys


class Bank:

    BANK_NAME = "Canara Bank"

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance+amt
        print(f'Hi {self.name} your balance in {Bank.BANK_NAME} is {self.balance}')

    def withdraw(self, amt):
        if amt < self.balance:
            self.balance = self.balance - amt
            print(f'Hi {self.name} your current balance in {Bank.BANK_NAME} is {self.balance} after withdrawing {amt}')
        else:
            sys.exit(f'thanks for banking with {Bank.BANK_NAME}')


print(f'Welcome to {Bank.BANK_NAME}')
name = input("Enter your name")
b = Bank(name)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option = input("Choose an option")
    if option.lower() =='d':
        amt = float(input("How much amount you want to deposit"))
        b.deposit(amt)
    elif option.lower() == 'w':
        amt = float(input("How much amount you want to withdraw"))
        b.withdraw(amt)
    else:
        sys.exit("bye")







