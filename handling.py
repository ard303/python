#file=open("code.txt",'a')
#print(file.read())
#file.close()

#file.write("introduce yourself")
#file.close()
#file.write("introduce yourself")
#file.close()

#file=open("code.txt",'r')
#content=file.read()
#counter=0
#lines=content.split("\n")
#for line in lines:
 #   if line:
  #      counter+=1

#print(counter)


f1=open("code.txt")
f2=open("empty.txt",'a')
content=f1.read()
f2.write(content)
f1.close()
f2.close()