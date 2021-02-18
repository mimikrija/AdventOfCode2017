# Day 15: Dueling Generators

from santas_little_helpers import *

# Generator A starts with 699
# Generator B starts with 124


def generate(start, multiplier, divisor=1):
    last_value = start
    while True:
        last_value *= multiplier
        last_value %= 2147483647
        if last_value % divisor == 0:
            yield last_value & 0b1111111111111111 # same as 0xffff


A = generate(699, 16807)
B = generate(124, 48271)

part_1 = sum(next(A) == next(B) for _ in range(40*1000*1000))

# part 2
A = generate(699, 16807, 4)
B = generate(124, 48271, 8)

part_2 = sum(next(A) == next(B) for _ in range(5*1000*1000))


print_solutions(part_1, part_2)
# Part 1 solution is: 600
# Part 2 solution is: 313
