file=open("text.txt", 'r')
print(file.read(8))
file.close()

file=open("text.txt",'a')
file.write("hello my name is ayan sajjad i am 17 year old")
file.close()