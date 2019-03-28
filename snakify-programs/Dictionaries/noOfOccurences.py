#The text is given in a single line. For each word of the text count the number of its occurrences before it.
# A word is a sequence of non-whitespace characters. Two consecutive words are separated by one or more spaces.
# Punctiation marks are a part of a word, by this definition.
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')