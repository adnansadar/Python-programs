# Given a number n, followed by n lines of text, print the number of distinct words
# that appear in the text.

# For this, we define a word to be a sequence of non-whitespace
# characters, seperated by one or more whitespace or newline characters. Punctuation marks are part of a word, in this definition.

n = int(input())
s=set()
for i in range(n):
    s.update(input().split())
print(len(s))
