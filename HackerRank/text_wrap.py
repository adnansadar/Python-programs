# Output Format
# Print the text wrapped paragraph.
# Sample Input:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])