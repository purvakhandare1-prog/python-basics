class Bankaccount:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print(f"current balance is {balance}")

    def withdrawl_money(self,amount):
        self.amount=amount
        if amount>=self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"your current balance {self.balance}")
            return self.balance

    def deposit(self,saving_amount):
        self.saving_amount=saving_amount
        self.balance += saving_amount
        print(f"now current balance {self.balance}")
        return self.balance


# Test
acc = Bankaccount("Priya", 5000)
acc.withdrawl_money(1000)
acc.deposit(2000)
