num=int(input("enter a number to check if it is a prime number"))
if(num>1):
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            print("it is not a prime number")
            break 
    else:
        print("it is a prime number")
else:
    print("it is not a prime number")            