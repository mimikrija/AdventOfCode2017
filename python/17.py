# Day 17: Spinlock
from santas_little_helpers import print_solutions
from collections import deque


def last_points_to(step, max_size):
    spinlock = deque([0])
    for size in range(1, max_size+1):
        spinlock.rotate(-step)
        spinlock.append(size)
    # using this approach the most recent element is always inserted at the end
    # hence, the last element 'points to' spinlock[0]
    return spinlock[0]


def insert_position(current_position, step, size):
    if current_position + step >= size:
        return (current_position + step) % size + 1
    else:
        return current_position + step + 1


def generate_zero_positions(step, insertions):
    pos = 0
    for size in range(1, insertions+1):
        pos = insert_position(pos, step, size)
        if pos == 1:
            solution = size
    yield solution


# my input
step = 386

part_1 = last_points_to(step, 2017)
part_2 = next(generate_zero_positions(step, 50000000))


print_solutions(part_1, part_2)
# Part 1 solution is: 419
# Part 2 solution is: 46038988
