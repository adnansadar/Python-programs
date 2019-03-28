r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
if(r2-r1!=1 and r2-r1!=-1 and r2-r1!=0):
    print("NO")
elif(c2-c1!=1 and c2-c1!=-1 and c2-c1!=0):
    print("NO")
else:
    print("YES")