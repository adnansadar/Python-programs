# Write a function capitalize(lower_case_word) that takes the lower case word and returns the word with
# the first letter capitalized. Eg., print(capitalize('word')) should print the word Word.
# Then, given a line of lowercase ASCII words (text separated by a single space), print it with the first letter
# of each word capitalized using the your own function capitalize().
def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - 97 + 65)
    return first_letter_big + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))