# Chocolate bar has the form of a rectangle divided into n×m portions.
# Chocolate bar can be split into two rectangular parts by breaking it
# along a selected straight line on its pattern. Determine whether
# it is possible to split it so that one of the parts will have exactly k squares.
# The program reads three integers: n, m, and k. It should print YES or NO.
a = int(input())
b = int(input())
c = int(input())
if((c>=a and c>=b) and (c%a==0 or c%b==0) and (a*b>=c)):
    print("YES")
else:
    print("NO")