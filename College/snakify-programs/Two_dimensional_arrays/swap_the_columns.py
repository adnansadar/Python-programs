#Given two positive integers m and n, m lines of n elements, giving an m×n matrix A,
#followed by two non-negative integers i and j less than n, swap columns i and j of A and print the result.
#Write a function swap_columns(a, i, j) and call it to exchange the columns. 

def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]

m, n = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
for row in a:
    print(' '.join([str(column) for column in row]))