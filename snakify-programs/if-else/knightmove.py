r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
if abs(r1-r2)==2 and abs(c1-c2)==1 or abs(c1-c2)==2 and abs(r1-r2)==1:
    print("YES")
else:
    print("NO")
