#for loop

for i in range(1,16,2):
    print(i)

#m table
    for i in range(1,15):
        print(i,"* 2 = ",i*2)

    
#multiplication table
num=(int(input("Enter the number")))
for i in range(1,15):
    print(i,"*",num,"=",i*num)

#task4
abarna=[]
num=(int(input("Enter the number")))
for i in range(1,15):
    a=i*num
    abarna.append(a)
print(abarna)
