n = int(input())
count = 0
#calculate no of zeros entered by user
for i in range(n):
    if(int(input())==0):
        count = count +1
print(count)