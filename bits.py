def numofbits(n):
    ones=0
    zeros=0

    while(n):
        if(n & 1 ==1):
            ones += 1
        else:
            zeros +=1
        n >>= 1
    print("number of ones ", ones ," and the number of zeros ",zeros)


number=int(input("enter the number "))
numofbits(number)