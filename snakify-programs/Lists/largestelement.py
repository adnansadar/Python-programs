#Given a list of numbers. Determine the element in the list with the largest value. Print the value of the largest element and then the index number. If the highest element is not unique, print the index of the first instance.

a=[int(i) for i in input().split()]
maxindex=0
for i in range(1,len(a)):
    if(a[i]>a[maxindex]):
        maxnum=a[i]
        maxindex=i
print(a[maxindex],maxindex)