#Given an odd number integer n, produce a two-dimensional array of size (n×n). Fill each element with a single character string of "." .
# Then fill the middle row, the middle column and the diagnals with the single character string of "*" (an image of a snow flake). 
# Print the array elements in (n×n) rows and columns and separate the characters with a single space. 
n = int(input())
l = [['.'] * n for i in range(n)]
for i in range(n):
    l[i][i] = '*'
    l[n // 2][i] = '*'
    l[i][n // 2] = '*'
    l[i][n - i - 1] = '*'
for row in l:
    print(' '.join(row))