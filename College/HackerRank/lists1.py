#Input Format

# The first line contains an integer,
# , denoting the number of commands.
# Each line of the

# subsequent lines contains one of the commands described above.

# Constraints

#     The elements added to the list must be integers.

# Output Format

# For each command of type print, print the list on a new line.
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l