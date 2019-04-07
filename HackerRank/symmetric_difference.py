#Given sets of integers, and , print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either or
# but do not exist in both.
# Input Format
# The first line of input contains an integer,
# .
# The second line contains space-separated integers.
# The third line contains an integer, .
# The fourth line contains
# space-separated integers.
# Output Format
# Output the symmetric difference integers in ascending order, one per line.

M=int(input())
l=[i for i in input().split()]
N=int(input())
l2=[i for i in input().split()]
a=set()
b=set()
a.update(l)
b.update(l2)
c=a^b
l=list(c)
l.sort()
for i in l:
    print(i)

