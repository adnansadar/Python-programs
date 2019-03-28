s=[int(i) for i in input().split()]
s2=" "
count=0
for i in range(0,len(s)):
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            break
    else:
        print(s[i], end=' ')