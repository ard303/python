from math import sqrt
num=int(input("enter a number to determine if it is a prime number : "))
if (num>1):
    for i in range(2,int(sqrt(num))+1):
        if(num%i==0):
            print(num," is not a prime number")
        
        else:
            print(num," is a prime number")

else:
    print(num,"is not a prime number")

