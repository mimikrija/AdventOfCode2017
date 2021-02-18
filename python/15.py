# Day 15: Dueling Generators

from santas_little_helpers import *

# Generator A starts with 699
# Generator B starts with 124


def generate(start, multiplier):
    last_value = start
    while True:
        last_value *= multiplier
        last_value %= 2147483647
        yield last_value & 0b1111111111111111 # same as 0xffff


A = generate(699, 16807)
B = generate(124, 48271)

part_1 = sum(next(A) == next(B) for _ in range(40*1000*1000))


print_solutions(part_1)
# Part 1 solution is: 600
