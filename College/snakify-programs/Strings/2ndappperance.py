#Given a string that may or may not contain the letter of interest.
# Print the index location of the second occurrence of the letter f. If the string contains the letter f only once, then print -1, and if the string does not contain the letter f, then print -2.
s=input()
if s.count("f")==1:
    print(-1)
elif s.count("f")==0:
    print(-2)
else:
    print(s.find("f",s.find("f")+1))