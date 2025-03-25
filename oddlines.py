file1=open('text.txt','r')
file2=open('filetofill.txt','a')

file=file1.readlines()

for i in range (0,len(file)):
    if (i%2!=0):
        file2.write(file[i])

file1.close()
file2.close()