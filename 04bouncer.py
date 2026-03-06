#The Bouncer: Ask the user for their age. If they are 18 or older, print "Welcome!" Otherwise, print "Access Denied."
user_age=int(input("enter your age:"))
if user_age>=18:
    print("welcome!")
else:
    print("acess denied.")