def fact(n):
    if(n==1):
        return n 
    else:
        return n*fact(n-1) 
num=int(input("enter a number whose factorial you want"))

if(num<0):
    print("there is no factorial of a negative number")
elif(num==0):
    print("the factorial of 0 is 1")
else:
    print("the factorial of ", num ,"is", fact(num))    