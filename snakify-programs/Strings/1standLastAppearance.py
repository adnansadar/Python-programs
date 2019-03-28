#Given a string that may or may not contain a letter of interest. Print the index location of the first
# and last appearance of f. If the letter f occurs only once, then output its index. If the letter f does not occur, then do not print anything.
s=input()
if s.count('f')==1:
    print(s.find('f'))
elif s.count('f')>1:
    print(s.find('f'),s.rfind('f'))