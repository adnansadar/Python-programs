#  The first line contains a single integer N — the number of English words in the dictionary. Followed by N dictionary
#  entries. Each entry is contained on a separate line, which contains first the English word, then a hyphen surrounded
#  by spaces and then comma-separated list with the translations of this English word in Latin. All the words consist
#  only of lowercase English letters. The translations are sorted in lexicographical order. The order of English words
#  in the dictionary is also lexicographic.
#
# Print the corresponding Latin-English dictionary in the same format. In particular, the first word line should be the
# lexicographically minimal translation of the Latin word, then second in that order, etc. Inside the line the English
# words should be sorted also lexicographically.

from collections import defaultdict

latin_to_english = defaultdict(list)
for i in range(int(input())):
    english_word, latin_translations_chunk = input().split(' - ')
    latin_translations = latin_translations_chunk.split(', ')
    for latin_word in latin_translations:
        latin_to_english[latin_word].append(english_word)

print(len(latin_to_english))
for latin_word, english_translations in sorted(latin_to_english.items()):
    print(latin_word + ' - ' + ', '.join(english_translations))

