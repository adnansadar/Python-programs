prevnum = int(input())
answer = 0
while prevnum != 0:
    nextnum = int(input())
    if nextnum != 0 and prevnum < nextnum:
        answer += 1
    prevnum = nextnum
print(answer)