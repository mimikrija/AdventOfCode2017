# Day 15: Dueling Generators

from santas_little_helpers import *

# Generator A starts with 699
# Generator B starts with 124


def generate_A():
    last_value = 699
    #last_value = 65
    while True:
        last_value *= 16807
        last_value %= 2147483647
        yield last_value & 0b1111111111111111

def generate_B():
    last_value = 124
    #last_value = 8921
    while True:
        last_value *= 48271
        last_value %= 2147483647
        yield last_value & 0b1111111111111111 # same as 0xffff


A = generate_A()
B = generate_B()

part_1 = sum(next(A) == next(B) for _ in range(40*1000*1000))

print_solutions(part_1)
# Part 1 solution is: 600
