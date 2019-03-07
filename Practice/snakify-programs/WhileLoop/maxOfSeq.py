num=int(input())
maxnum=num
while(num!=0):
    if(num>maxnum):
        maxnum=num
    num=int(input())
print(maxnum)