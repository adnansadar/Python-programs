a = int(input())
temp = a
sum = 0
while(temp!=0):
    dig = int(temp%10)
    sum = sum + dig
    temp = temp//10
print(sum)