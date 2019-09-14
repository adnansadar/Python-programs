#Given a list of numbers with all of its elements sorted in ascending order, determine and
# print the quantity of distinct elements in it.
l=[int(i) for i in input().split()]
count=1
for i in range(1,len(l)):
    if l[i]!=l[i-1]:
        count+=1
print(count)