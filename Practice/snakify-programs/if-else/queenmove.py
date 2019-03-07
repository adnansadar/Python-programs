r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
if (abs(r1-r2)) == (abs(c2-c1)):
    print("YES")
elif abs(r1-r2)==0 and abs(c1-c2)!=0:
    print("YES")
elif abs(c1-c2)==0 and abs(r1-r2)!=0:
    print("YES")
else:
    print("NO")