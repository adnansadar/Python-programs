max1 = int(input())
max2 = int(input())
if max1 < max2:
    max1, max2 = max2, max1
num = int(input())
while num != 0:
    if num > max1:
        max2, max1 = max1, num
    elif num > max2:
        max2 = num
    num = int(input())
print(max2)