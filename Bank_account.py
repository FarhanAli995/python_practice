class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        acc_no = float(input("enter your account number:"))

    def debit(self, amount):
        amount = float(input("enter your debited amount"))
        self.balance -= amount
        print("Rs",amount,"was debitted")
        print("Your total balance is now:", self.get_bal())

    def credit(self,amount):
        amount = float(input("enter your crediting amount:"))
        self.balance += amount
        print("Rs",amount,"was credited")
        print("Your Total balance is now:",self.get_bal())

    def get_bal(self):
        return self.balance

acc1 = Account(1000, 12345)
acc1.get_bal()
acc1.debit(0)
acc1.credit(0)

        
        