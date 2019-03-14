s=set()
l=[int(i) for i in input().split()]
for j in l:
    if j in s:
        print("YES")
    else:
        print("NO")
        s.add(j)