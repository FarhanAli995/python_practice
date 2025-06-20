# Abstraction:
#  Hiding the implementation details of a class and only showing the essential features to the user.

#  Encapsulation:
#  Wrapping data and functions into a single unit (object).
#  Apna Colleg

#inheritance:

#polymorphism:

class Account:
    def __init__(self, balance,acc_No):
        self.balance = balance
        self.acc_No = acc_No

    def debit(self, amount):
        self.balance -= amount
        print("Rs",amount,"was debitted")
        print("your total balance is now:", self.get_bal())

    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited")
        print("Your Total balance is now:",self.get_bal())

    def get_bal(self):
        return self.balance

acc1 = Account(1000, 12345)
acc1.get_bal()
acc1.debit(500)
acc1.credit(5000)







        
