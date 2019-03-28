#Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). Print the resulting list.
# If a list has an odd number of elements, leave the last element in place.

l = [int(i) for i in input().split()]
for i in range(1, len(l), 2):
    l[i - 1], l[i] = l[i], l[i - 1]
print(' '.join([str(i) for i in l]))