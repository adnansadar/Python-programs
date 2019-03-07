r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
if abs(r1-r2)%2!=0:
    if abs(c1-c2)%2!=0:
        print("YES")
    else:
        print("NO")
else:
    if abs(c1-c2)%2==0:
        print("YES")
    else:
        print("NO")