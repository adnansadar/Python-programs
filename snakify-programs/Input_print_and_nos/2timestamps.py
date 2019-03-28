h1 = int(input())#hour1
m1 = int(input())#minute1
s1 = int(input())#seconds1
h2 = int(input())
m2 = int(input())
s2 = int(input())
htotal = (h2-h1)*60*60#diff between h1 and h2
mtotal = (m2-m1)*60
stotal = s2-s1
total = htotal + mtotal + stotal#total time difference
print(total)