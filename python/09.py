# Day 9: Stream Processing

from santas_little_helpers import *
from collections import deque

def count_groups(braces):
    counter = []
    while len(braces) > 0:
        before = len(braces)
        braces = braces.replace('{}','')
        after = len(braces)
        counter.append((before-after)//2)
    print(counter)
    return counter

stream = deque(get_input('inputs/09')[0])

opened_braces = 0
closed_braces = 0
depth = 0
braces = []
braces_deq = deque()
solution = [0]
while stream:
    current = stream.popleft()
    if current == '{':
        opened_braces += 1
        braces.append('{')
        braces_deq.append('{')
        depth += 1
    if current == '}':
        solution.append(len(braces_deq))
        closed_braces += 1
        braces.append('}')
        depth -= 1
        braces_deq.pop()
        
    if current == '<':
        while current != '>':
            current = stream.popleft()
            if current == '!':
                stream.popleft()
    # if depth >= solution[-1]:
    #     solution.append(depth)



#print(solution)


# all_braces = ''.join(c for c in braces)



# part_1 = sum(count*val for val, count in enumerate(reversed(count_groups(all_braces)),1))

part_1 = sum(solution)
print_solutions(part_1)

# not 3338 too low
# not 21704 too high
