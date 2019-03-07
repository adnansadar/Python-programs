n1 = int(input("Enter a no: "))
temp = n1
n2 = 0
while(temp!= 0):
    dig = int(temp%10)
    n2 = int(dig**3 + n2)
    temp = int(temp/10)
if(n1 == n2):
    print("It is an armstrong no")
else:
    print("It is not an armstrong no")
