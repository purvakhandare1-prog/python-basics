# Ek function likhiye jo ek number n le aur check kare ki wo Prime hai ya nahi.
# Twist: Aapko loop ko $n$ tak nahi, balki sirf $\sqrt{n}$ tak chalana hai (efficiency ke liye).
# Logic: Agar number divisible nahi hai $\sqrt{n}$ tak, toh wo aage bhi nahi hoga.

def check_prime(n):
    if n%1==0 and n%n==0:
        return "prime"
    else:
       return "no prime"
result=check_prime(5)
print(result)

