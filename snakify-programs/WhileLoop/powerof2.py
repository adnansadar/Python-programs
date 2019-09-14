#For a given integer N, find the greatest integer x where 2x is less than or equal to N. Print the exponent value and the result of the expression 2x.
#Don't use the operation **.


n = int(input())
twopower = 2
power = 1
while twopower <= n:
    twopower *= 2
    power += 1
print(power - 1, twopower // 2)