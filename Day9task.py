
#task1
num1=int(input("Enter the First Number:"))
num2=int(input("Enter the second Number:"))
s=(input("Enter the symbol:"))
if s=="+":
    c=num1+num2
    print("addition is:",c)
elif s=="-":
    c=num1-num2
    print("subraction is:",c)
elif s=="*":
    c=num1*num2
    print("multiplication is:",c)
elif s=="/":    
    c=num1/num2
    print("division is:",c)
elif s=="%":
    c=num1%num2
    print("modulus is:",c)
else:
    print("Enter arithmetic symbols only")

#function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def calc():
    n1=int(input("Enter the First Number:"))
    n2=int(input("Enter the second Number:"))
    s=(input("Enter the symbol:"))
    if s=="+":
        print({add(n1,n2)})
    elif s=="-":
        print({sub(n1,n2)})
    elif s=="*":
        print({mul(n1,n2)})
    elif s=="/":
        print({div(n1,n2)})
    elif s=="%":
        print({mod(n1,n2)})
calc()
