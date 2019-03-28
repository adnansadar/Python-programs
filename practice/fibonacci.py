# def Fibonacci(n):
#     if n<0:
#         print("Incorrect input")
#     # First Fibonacci number is 0
#     elif n==0:
#         return 0
#     # Second Fibonacci number is 1
#     elif n==1:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(a,b,end=" ")
for i in range(n-2):
    c = a + b
    a = b
    b = c
    print(c , end = " ")