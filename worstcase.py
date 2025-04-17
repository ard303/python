def onsquaretime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end =" ")
            iteration+=1
        print("")
    print("when number is ",n,"iterations=",iteration)


#onsquaretime(4)
onsquaretime(6)