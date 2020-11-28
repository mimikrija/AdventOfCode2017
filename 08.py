import re

with open('./inputs/08-ex') as f:
    instructions = f.readlines()

words = re.compile(r'[a-z]+')
numbers = re.compile(r'[-]?\d+')
conditions = re.compile(r'[^a-z0-9- ]+')

for line in instructions:
    print(line)
    print(re.findall(words,line))
    print(re.findall(numbers,line))
    print(re.findall(conditions,line.strip()))