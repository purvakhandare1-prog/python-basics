def decorator(func):
    def wrapper(*args,**kwargs):
        if args[0]<0:
            print("negative")
        elif args[0]>100:
            print("❌ Marks 100 se zyada nahi ho sakte!")
        else:
            func(*args,**kwargs)
    return wrapper        

@decorator
def check(args):
    print("your output is:")
           
check(1003)
            
