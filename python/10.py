# Day 10: Knot Hash

from santas_little_helpers import *
from collections import deque

def tie_the_knots(lengths, size):
    circle = deque(num for num in range(size))


    current_pos = 0
    skip_size = 0

    for length in lengths:
        if length > size:
            continue
        #print(circle)
        for _ in range(current_pos):
            circle.append(circle.popleft())
        rev = []
        #print(circle)
        for _ in range(length):
            rev.append(circle.popleft())
        for num in rev:
            circle.appendleft(num)
        #print(circle)
        for _ in range(current_pos):
            circle.appendleft(circle.pop())
        current_pos += length + skip_size
        skip_size += 1
        current_pos %= size
        #print(circle, length, current_pos)


    return circle[0] * circle[1]


lengths = [3, 4, 1, 5]
lengths = [165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153]
size = 5
size = 256

part_1 = tie_the_knots(lengths, size)
print_solutions(part_1)
# Part 1 solution is: 4114
