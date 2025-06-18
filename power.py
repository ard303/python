def power(num):
    if num <= 0:
        return False
    return (num & (num-1))==0




n=int(input("enter the number"))
if(power(n)):
       print("the number is a power of 2")
else:
        print("number is not the power of 2")