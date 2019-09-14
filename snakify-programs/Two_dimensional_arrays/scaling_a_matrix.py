#Given two positive integers m and n, m lines of n elements, giving an m×n matrix A,
# followed by one integer c, multiply every entry of the matrix by c and 
# print the result.


m,n=[int(i) for i in input().split()]
l=[[int(i) for i in input().split()]for j in range(m)]
c= int(input())
for i in range (m):
    for j in range(n):
        l[i][j] *= c
for row in l:
    print(' '.join([str(column) for column in row]))