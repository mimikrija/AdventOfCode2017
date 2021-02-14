# Day 10: Knot Hash

from santas_little_helpers import *
from collections import deque
from operator import xor
from functools import reduce

def tie_the_knots(lengths, size, in_circle=None, current_pos=0, skip_size=0):
    if not in_circle:
        circle = deque(num for num in range(size))
    else:
        circle = in_circle

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


    return circle, current_pos, skip_size


def sparse_hash(lengths):
    current_pos, skip_size = 0, 0
    for knot_round in range(64):
        if knot_round == 0:
            circle = None
        circle, current_pos, skip_size = tie_the_knots(lengths, size, circle, current_pos, skip_size)
        #print(knot_round, current_pos, skip_size)
    return circle

def dense_hash_hex(in_circle):
    circle = list(in_circle)
    dense = [reduce(xor, circle[n*16:(n+1)*16]) for n in range(16)]
    hexes = [int(str(num), 16) for num in dense]
    hexes_2 = [hex(num) for num in dense]
    return ''.join('{:02x}'.format(num) for num in dense)



lengths = [165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153]
size = 256

part_1_circle, _, _ = tie_the_knots(lengths, size)
part_1 = part_1_circle[0]*part_1_circle[1]


# part 2 new specifications

lengths_2 = [ord(c) for c in ','.join(str(num) for num in lengths)] + [17, 31, 73, 47, 23]

part_2 = dense_hash_hex(sparse_hash(lengths_2))


print_solutions(part_1, part_2)
# Part 1 solution is: 4114
# Part 2 solution is: 2f8c3d2100fdd57cec130d928b0fd2dd
