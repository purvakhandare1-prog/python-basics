class Bankaccount:

    def  __init__(self,name,balance):
      self.name=name
      self.__balance=balance
    

    def get_show(self):
      return self.__balance
      

    def set_balance(self,amount):
       if amount>=self.__balance:
            print("insufficient balance")
       else:
            self.__balance-=amount
            print(f"your current balance{self.__balance}")
            return self.__balance
       
a=Bankaccount("purva",1000)
a.get_show()
a.set_balance(600000)
    
