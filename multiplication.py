#num=10
#for i in range(1,11):
 #   print("10 x" , i , " = " , num*i)
num=int(input("enter the number of rows "))
for i in range(1,num+1):
    for j in range(i):
        print("*", end=" ")
    print()
