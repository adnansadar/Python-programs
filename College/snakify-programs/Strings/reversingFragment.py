#Given a string in which the letter h occurs at least two times, reverse the sequence of characters
# enclosed between the first and last appearances.
s = input()
a = s[:s.find('h')+1]
b = s[s.find('h'):s.rfind('h')]
c = s[s.rfind('h')+1:]
print(a+b[::-1]+c)