#Given a list of countries and cities of each country. Then given the names of the cities. For each city specify
# the country in which it is located.

n=int(input())
land = {}
for i in range(n):
    country, *cities = input().split()
    for city in cities:
        land[city] = country
n2=int(input())
for i in range(n2):
    print(land[input()])