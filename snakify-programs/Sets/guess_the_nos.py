# Augustus and Beatrice play the following game. Augustus thinks of a secret integer number from 1 to n.
#  Beatrice tries to guess the number by providing a set of integers. Augustus answers YES
#  if his secret number exists in the provided set, or NO, if his number does not exist in the provided numbers.
#   Then after a few questions Beatrice, totally confused, asks you to help her determine Augustus's secret number.
#  Given the value of n
#  in the first line, followed by the a sequence Beatrice's guesses, series of numbers seperated by spaces and Agustus's responses, or Beatrice's plea for HELP.
#  When Beatrice calls for help, provide a list of all the remaining possible secret numbers, in ascending order, separated by a space.

num = int(input())
all_nums = set(range(1, num + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    ans = input()
    if ans == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))