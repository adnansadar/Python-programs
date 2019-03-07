#Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.

s = input()
a = s[:s.find('h')+1]
b = s[s.find('h')+1:s.rfind('h')]
c = s[s.rfind('h'):]
print(a+b.replace('h','H')+c)