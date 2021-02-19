# Day 17: Spinlock
from santas_little_helpers import print_solutions

step = 386
#step = 3

# circular linked list {position: points_to}
circle = {0: 0}
last = 0

for pos in range(2017+1):
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
print_solutions(part_1)
# Part 1 solution is: 419
