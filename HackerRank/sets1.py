#Input Format
# The first line contains the integer,
# the total number of plants.
# The second line contains the
# space separated heights of the plants.
# Constraints
# Output Format
# Output the average height value on a single line.
def average(array):
    avg=sum(set(array))/len(set(array))
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
