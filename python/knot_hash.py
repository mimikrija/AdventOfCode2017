# stuff needed by day 10 and day 14

from collections import deque
from operator import xor
from functools import reduce

def tie_the_knots(lengths, in_circle=None, current_pos=0, skip_size=0, size=256):
    if not in_circle:
        circle = deque(num for num in range(size))
    else:
        circle = in_circle

    for length in lengths:
        if length > size:
            continue
        for _ in range(current_pos):
            circle.append(circle.popleft())
        rev = []
        for _ in range(length):
            rev.append(circle.popleft())
        for num in rev:
            circle.appendleft(num)
        for _ in range(current_pos):
            circle.appendleft(circle.pop())
        current_pos += length + skip_size
        skip_size += 1
        current_pos %= size

    return circle, current_pos, skip_size


def sparse_hash(lengths):
    current_pos, skip_size = 0, 0
    for knot_round in range(64):
        if knot_round == 0:
            circle = None
        circle, current_pos, skip_size = tie_the_knots(lengths, circle, current_pos, skip_size)
    return circle


def dense_hash(in_circle, hash_type='hex'):
    circle = list(sparse_hash(generate_lengths(in_circle)))
    dense = (reduce(xor, circle[n*16:(n+1)*16]) for n in range(16))

    if hash_type == 'hex':
        return ''.join('{:02x}'.format(num) for num in dense)
    if hash_type == 'bin':
        return ''.join('{:02b}'.format(num) for num in dense)


def generate_lengths(in_lengths):
    if isinstance(in_lengths, list):
        input_string = ','.join(str(num) for num in in_lengths)
    else:
        input_string = in_lengths
    return [ord(c) for c in input_string] + [17, 31, 73, 47, 23]
