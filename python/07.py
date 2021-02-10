import collections

import re


words = re.compile(r'[a-z]+')
numbers = re.compile(r'[-]?\d+')
conditions = re.compile(r'[^a-z0-9- ]+')

for line in instructions:
    bla = re.findall(words,line)

def is_same(configuration):
    return len(set(configuration)) == 1

def who_is_unique(input_collection):
    count_stuff = collections.Counter(input_collection)
    for thing in count_stuff:
        if count_stuff[thing] == 1:
            return(thing)
    return None

def who_is_common(input_collection):
    count_stuff = collections.Counter(input_collection)
    for thing in count_stuff:
        if count_stuff[thing] > 1:
            return(thing)
    return None

def calculate_weight(node):
    weight = program_dict[node][0]
    if program_dict[node][1] != []:
        for child in program_dict[node][1]:
            weight += calculate_weight(child)
    return weight

def who_is_unbalanced(node):
    weights = {}
    if program_dict[node][1] == []:
        return None
    else:
        for child in program_dict[node][1]:
            weights[child] = calculate_weight(child)
        if who_is_unique(weights.values()) == None:
            return None
        else:
            who = list(weights.values()).index(who_is_unique(weights.values()))
            return list(weights.keys())[who]


all_programs = []
all_inputs = []

with open('./inputs/07', 'r') as infile:
    for line in infile.readlines():
        for word in line.split():
            if word != '->' and '(' not in word:
                all_programs.append(word.replace(',',''))
        all_inputs.append(line)

program_dict = {}

# parse input for part 2
for line in all_inputs:
    s = line.index('(')
    e = line.index(')')
    line = line.strip()
    node = line[0:s-1]
    weight = line[s+1:e]
    if '->' in line:
        children = (line.split('-> ')[1]).split(', ')
    else:
        children = []
    program_dict[node] = [int(weight),children]

solution_1 = who_is_unique(all_programs)

# part 2
current = solution_1
while True:
    if who_is_unbalanced(current) == None:
        break
    previous = current
    current = who_is_unbalanced(current)

neighbor_weights = [ calculate_weight(child) for child in program_dict[previous][1] ]

solution_2 = program_dict[current][0] + who_is_common(neighbor_weights) - who_is_unique(neighbor_weights)

print(f"The program at the bottom is: {solution_1}!")
# The program at the bottom is: hlhomy!

print(f"The weight of the unbalanced program should be: {solution_2}!")
# The weight of the unbalanced program should be: 1505!
