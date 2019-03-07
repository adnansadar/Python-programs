#Printing nos from a to b inclusively
a = int(input())
b = int(input())
#printing in ascending order if a<b
if a<b:
    for i in range(a,b+1):
        print(i,end=" ")
#printing in descending order if a>=b
else:
    for i in range(a,b-1,-1):
        print(i,end=" ")