# Day 9: Stream Processing

from santas_little_helpers import *
from collections import deque



stream = deque(get_input('inputs/09')[0])


braces_deq = deque()
solution = []
garbage = []
while stream:
    current = stream.popleft()
    if current == '{':
        braces_deq.append('{')
    if current == '}':
        solution.append(len(braces_deq))
        braces_deq.pop()
    if current == '<':
        while current != '>':
            current = stream.popleft()
            if current == '!':
                stream.popleft()
                continue
            if current != '>':
                garbage.append(current)

part_1 = sum(solution)
part_2 = len(garbage)
print_solutions(part_1, part_2)

# Part 1 solution is: 10616
# Part 2 solution is: 5101
