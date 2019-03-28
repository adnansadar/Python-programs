#Given two numbers n and m. Create a two-dimensional array of size (n×m)
# and populate it with the characters "." and "*" in a checkerboard pattern.
# The top left corner should have the character "." . 
n,m=[int(i) for i in input().split()]
l=[]
for i in range(n):
    l.append([])
    for j in range(m):
        if i%2==0 and j%2!=0:
            l[i].append('*')
        elif i%2!=0 and j%2==0:
            l[i].append('*')
        else:
            l[i].append('.')
for k in l:
    print(' '.join(k))