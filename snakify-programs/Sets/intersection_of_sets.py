# Given two lists of numbers. Find all the numbers that occur in both the first and the second list and print them in ascending order.
print(*sorted(set(input().split())&(set(input().split())))