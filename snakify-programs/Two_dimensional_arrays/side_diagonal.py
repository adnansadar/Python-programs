#Given an integer n, create a two-dimensional array of size (n×n) and populate it as follows, with spaces between each character:
	#The positions on the minor diagonal (from the upper right to the lower left corner) receive 1 .
    #The positions above this diagonal recieve 0 .
    #The positions below the diagonal receive 2 . 

Print the elements of the resulting array. 
n = int(input())
L=[[2 for i in range(n)] for j in range(n)]
k=n-1
for i in range(n):
	for j in range(n):
		if j<k:
			L[i][j]=0
		elif j==k:
			L[i][j]=1
		else:
			L[i][j]=2
	k-=1
for i in L:    
    print(' '.join([str(j) for j in i]))
