num=int(input("enter number: "))
orignalnum=num
reversenum=0

while (num>0):
    digit=num%10
    reversenum=reversenum*10+digit
    num //=10

if (orignalnum==reversenum):
    print("the number is a palindrome number")

else:
    print("the number is not a palindrome number")