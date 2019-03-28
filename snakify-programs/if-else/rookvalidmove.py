r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
if(r1>r2 and c1!=c2 or r1<r2 and c1!=c2):
    print("NO")
elif(c1>c2 and r1!=r2 or c1<c2 and r1!=r2):
    print("NO")
else:
    print("YES")