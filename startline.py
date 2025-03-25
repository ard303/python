file1=open('text.txt','r')
file2=open('filetofill.txt','a')

for line in file1.readlines():

    if not(line.startswith("coding")):
        print(line)
        file2.write(line)

file1.close()
file2.close()