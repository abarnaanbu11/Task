#task1
str1="abarnaanbu"
str2="abarnaanbu11@gmail.com"
str3="abar0013"
num=(input("Enter the user name:"))
num1=(input("Enter user mailid:"))
num2=(input("enter password:"))
if num==str1 and num1==str2 and num2==str3:
    print("correct")
else:
    print("incorrect")
#task2

num=int(input("enter the number:"))
if num<=9:
    print("single digit number")
elif num<100:
    print("double digit number")
elif num<1000:
    print("three digit numbert")
elif num<10000:
    print("four digit numbert")
elif num<10000:
    print("five digit numbert")
else:
    print("nothing")

#marklist
s1=int(input("Enter mark1:"))
s2=int(input("Enter mark2:"))
s3=int(input("Enter mark3:"))
s4=int(input("Enter mark4:"))
s5=int(input("Enter mark5:"))
tot=s1+s2+s3+s4+s5
tot1=tot/5
print(tot)
print(tot1)
if tot1<25:
    print("grade is fail")
elif tot1>25 and tot1<45:
    print("grade is E")
elif tot1>45 and tot1<50:
    print("grade is D")
elif tot1>50 and tot1<60:
    print("grade is C")
elif tot1>60 and tot1<80:
    print("grade is B")
elif tot1>80:
    print("grade is B")
else:
    print("invalid")

#class
n1=int(input("number of classes held:"))
n2=int(input("number of classes attendt:"))
print(n1)
print(n2)
cls=n2/n1*100
print(cls)
if cls<75:
    print("student not allowd to exam")
else:
    print("Student allowed to exam")



       
       




