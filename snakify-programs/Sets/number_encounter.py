# Given a sequence of numbers, determine if the next number has already been encountered.
# For each number, print the word YES (in a separate line) if this number has already been encountered,
# and print NO, if it has not already been encountered.
s=set()
l=[int(i) for i in input().split()]
for j in l:
    if j in s:
        print("YES")
    else:
        print("NO")
        s.add(j)