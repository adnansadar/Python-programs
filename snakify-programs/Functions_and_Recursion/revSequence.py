# Given a sequence of integers that end with a 0. Print the sequence in reverse order.
def rev():
    num=int(input())
    if num!=0:
        rev()
    print(num)
rev()