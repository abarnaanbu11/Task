# while 1
n = 0
while True:
    n += 1
    print(n, "Abarna")
    if n == 10:
        break

# while 2
abar = []   # for even numbers
abarl = []  # for odd numbers
n = 0

while n <= 100:
    if n % 2 == 0:
        abar.append(n)
    else:
        abarl.append(n)
    n += 1
print("Even numbers:", abar)
print("Odd numbers:", abarl)