n=int(input())
land = {}
for i in range(n):
    country, cities = input().split()
    for city in cities:
        land[city] = country
n2=int(input())
for i in range(n2):
    print(land[input()])
