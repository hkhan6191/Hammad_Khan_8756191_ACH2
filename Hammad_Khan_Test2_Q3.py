class Account(object):
    def __init__(self):
        self.balance = 0
    
    def deposit(self):
        depositInput = float(input("Please enter in the amount you wish to deposit: "))
        self.balance = self.balance + depositInput
        print("Deposit successful! Your current balance is: $%.2f" % self.balance)

    def withdrawal(self):
        withdrawInput = float(input("Please enter in the amount you wish to withdraw: "))
        if self.balance >= withdrawInput:
            self.balance = self.balance - withdrawInput
            print("Withdrawal successful! Your current balance is: $%.2f" % self.balance)

        else:
            print("Insufficient funds.")

    def finBalance(self):
        print("Your current balance is: $%.2f" % self.balance)

x = Account()
x.deposit()

choice = int(input("Do you wish to deposit money or withdraw money (1:Deposit, 2:Withdraw): "))
if choice == 1:
    x.deposit()

elif choice == 2:
    x.withdrawal()

x.finBalance() 