import collections

all_programs = []

with open('./inputs/07', 'r') as infile:
    for line in infile.readlines():
        for word in line.split():
            if word != '->' and '(' not in word:
                all_programs.append(word.replace(',',''))


count_programs = collections.Counter(all_programs)

for word in count_programs:
    if count_programs[word] == 1:
         solution_1 = word
         break

print(f"The program at the bottom is: {solution_1}!")
# The program at the bottom is: hlhomy!