
def check_balance(func):
     def wrapper(*args,**kwargs):
          if args[0]<0:
               print("invalid amount")
          else:
               func(*args,**kwargs)
     return wrapper


def check_pin(func):
     def wrapper(*args,**kwargs):
          if args[1]!="1234":
               print("invalid")
          else:
               func(*args,**kwargs)
     return wrapper

@check_balance
@check_pin
def withdraw(money,pin):
     print("your output is") 




withdraw(-99999,"1111")


            
