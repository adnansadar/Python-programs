l=input()
maxcount=1
count=1
for i in range(len(l)-1):
        for j in range(i+1,len(l)):
                if l[i]!=l[j]:
                        count+=1
        if count>maxcount:
                maxcount=count
        count=1
print(maxcount)
        
                
