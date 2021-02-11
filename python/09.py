# Day 9: Stream Processing

from santas_little_helpers import *
from collections import deque


def process_stream(stream):

    braces = deque()
    groups = 0
    garbage = 0

    while stream:
        current = stream.popleft()
        if current == '{':
            braces.append('{')
        if current == '}':
            # close group
            groups += len(braces)
            braces.pop()
        # garbage
        if current == '<':
            while True:
                current = stream.popleft()
                if current == '!':
                    stream.popleft()
                    continue
                if current == '>':
                    break
                else:
                    garbage += 1

    return groups, garbage


stream = deque(get_input('inputs/09')[0])
print_solutions(*process_stream(stream))

# Part 1 solution is: 10616
# Part 2 solution is: 5101
