t1 = input("Enter a string: ")
l = len(t1)
for i in range(0,l):
    if(t1[i]==t1[l-1-i]):
        k=1
    else:
        k=0
if(k ==1):
    print("Palindrome")
else:
    print("Not palindrome")