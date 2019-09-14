d1 = int(input("Enter date 1: "))
m1 = int(input("Enter month 1: "))
d2 = int(input("Enter date 2: "))
m2 = int(input("Enter month 2: "))
if (m2>=m1) and (d2>d1):
	dmonths = (m2-m1)*30
	ddates = dmonths + (d2 - d1)
elif (m2>=m1) and (d1>d2):
	dmonths = (m2-m1)*30
	ddates = dmonths + (d1 - d2)
elif (m1>=m2) and (d2>d1):
	dmonths = (m1-m2)*30
	ddates = dmonths + (d2 - d1)
else:
	dmonths = (m1-m2)*30
	ddates = dmonths + (d1 - d2)
print("Difference in dates is:",ddates)
