#task 1
num=int(input("Enter the number:"))
if(num%2==0):
    print("given number is even number")
else:
    print("given number is odd")


# task 2
num=int(input("enter the age:"))
if(num>=18):
    print("you are eligible voter")
else:
    print("you are noteligible voter")

#task 3

number=int(input("Enter the number:"))
if(number%3==0 and number%5==0):
    print("fizz Buzz")
elif(number%5==0):
    print("Buzz")
elif(number%3==0):
    print("fizz buzz")
else:
    print("nothing")
