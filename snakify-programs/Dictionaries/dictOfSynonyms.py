#You are given a dictionary consisting of word pairs. Every word is a synonym the other word in its pair.
# All the words in the dictionary are different.
#After the dictionary there's one more word given. Find a synonym for him.

d={}
n=int(input())
for i in range(n):
    one,two=input().split()
    d[one]=two
    d[two]=one
print(d[input()])