n = int(input("Enter a no: "))
f = 1
if (n < 0):
    print("Factorial is not possible")
elif (n == 0):
    print("Factorial is: 1")
else:
    for i in range(1,n+1):
        f = f * i
    print("Factorial of the no is:",f)

