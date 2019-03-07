# Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour.
# Input and output in this problems are floating-point numbers.
num = float(input())
if(num>=30):
    t = int(num/30)
else:
    t = 0
num = num - (30*t)
d = num * 12
print(d)