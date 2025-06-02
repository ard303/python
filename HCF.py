largenum=int(input("enter the largest number:"))
smallnum=int(input("enter the smallest number:"))
while (smallnum):
    storenum=smallnum
    smallnum=largenum % smallnum
    largenum=storenum

print("the HCF is ", largenum)