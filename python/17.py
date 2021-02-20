# Day 17: Spinlock
from santas_little_helpers import print_solutions


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


# circular linked list {position: points_to}
circle = {0: 0}
last = 0

for pos in range(1,2017+1):
    # insert element into a linked list
    last_points_to = circle[last]
    circle[last] = pos
    circle[pos] = last_points_to
    last = pos
    for _ in range(step % (pos+1)):
        # step forward step steps
        last_points_to = circle[last]
        last = last_points_to


part_1 = circle[2017]
part_2 = next(generate_zero_positions(step, 50000000))


print_solutions(part_1, part_2)
# Part 1 solution is: 419
# Part 2 solution is: 46038988
