num = int(input())
count = 1
maxcount = count
maxnum = num
while (num != 0):
    if num > maxnum:
        maxnum = num
        maxcount = count
    count += 1
    num = int(input())
print(maxcount)
