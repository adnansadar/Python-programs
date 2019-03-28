# A cupcake costs A dollars and B cents.
# Determine, how many dollars and cents should one
# pay for N cupcakes. A program gets three numbers:
#     A, B, N. It should print two numbers:
#     total cost in dollars and cents.
a = int(input())
b = int(input())
n = int(input())
at = a*n
bt = b*n
if(bt>=100):
    d = bt // 100
    bt = bt % 100
    at = at + d
print(at,bt)
