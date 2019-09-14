#Each student at a certain school speaks a number of languages. We need to determine which languges
#are spoken by all the students, which languages are spoken by at least one student.
#Given, the number of students, and then for each student given the number of languages they speak
#followed by the name of each language spoken, find and print the number of languages spoken by all the students,
#followed by a list the languages by name, then print the number of languages spoken by at least one student,
#followed by the list of the languages by name. Print the languages in alphabetical order.

s = [{input() for j in range(int(input()))} for i in range(int(input()))]
everyone, someone = set.intersection(*s), set.union(*s)
print(len(everyone), *sorted(everyone), sep='\n')
print(len(someone), *sorted(someone), sep='\n')