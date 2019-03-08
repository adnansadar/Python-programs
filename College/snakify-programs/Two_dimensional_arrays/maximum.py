#Given two integers representing the rows and columns (m×n), and subsequent m rows of n elements,
 #find the index position of the maximum element and print two numbers representing the index (i×j)
 #or the row number and the column number. If there exist multiple such elements in different rows,
 #print the one with smaller row number. If there multiple such elements occur on the same row, output
 #the smallest column number.
m,n = [int(i) for i in input().split()]
l = [[int(j) for j in input().split()] for i in range(m)]
max_i, max_j = 0, 0
curr_max = l[0][0]
for i in range(m):
    for j in range(n):
        if l[i][j] > curr_max:
            curr_max = l[i][j]
            max_i, max_j = i, j
print(max_i, max_j)