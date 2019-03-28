# H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
# Determine the angle (in degrees) of the hour hand on the clock face right now.
h = int(input())
m = int(input())
s = int(input())
ha = 30*h
ma = 0.5*m
sa = 0.00833333*s
ta = ha + ma + sa
print(ta)