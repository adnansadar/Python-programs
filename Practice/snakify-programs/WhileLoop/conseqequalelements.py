#Given a sequence of integer numbers ending with the number 0. Determine the length of the widest fragment where
# all the elements are equal to each other.
prevnum=int(input())
nextnum=int(input())
currlen=1
maxlen=1
while(nextnum!=0):
    if(nextnum==prevnum):
        currlen+=1
        if currlen>maxlen:
            maxlen=currlen
    else:
        currlen=1
    prevnum,nextnum=nextnum,prevnum
    nextnum=int(input())
print(maxlen)