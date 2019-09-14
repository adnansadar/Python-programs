count=0
a=[int(i) for i in input().split()]
for i in range(1,len(a)-1):
    if a[i+1]<a[i] and a[i]>a[i-1]:
        count+=1
print(count)