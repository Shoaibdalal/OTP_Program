def my_function(a):
    if a == "OTP":
        import random
        f= random.randrange(100000,999999,3)
        return f
    else :
        return "something went to wrong"

t=str(input("Enter the String : "))
l=my_function(t)
print(l)

