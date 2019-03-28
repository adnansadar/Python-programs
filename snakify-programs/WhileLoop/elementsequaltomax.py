n = int(input())
maxn=n
count=0
while(n!=0):
    if(n>maxn):
        maxn=n
        count=1
    elif(n==maxn):
        count+=1
    n=int(input())
print(count)