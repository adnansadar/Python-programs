# A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers?
# The program gets two numbers: N and M.
import math
n = int(input())#km covered by car in 1 day
m = int(input())#total no of kms to be covered
print(math.ceil(m/n))