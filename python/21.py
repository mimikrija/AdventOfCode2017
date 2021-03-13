# Day 21: Fractal Art

from santas_little_helpers import *
import numpy as np


def all_configurations_of(in_rule):

    def flip_horizontal(in_rule):
        rows = in_rule.split('/')
        return '/'.join(rows[::-1])

    def transpose(in_rule): # this should be a transpose
        rows = [''.join(c for c in trans) for trans in zip(*in_rule.split('/'))]
        return '/'.join(rows)

    config = str(in_rule)
    configs = {config}

    for _ in range(4):
        config = transpose(config)
        configs.add(config)
        config = flip_horizontal(config)
        configs.add(config)
    return configs


def expand_rules(in_rules):
    """ expands the current set of rules with all possible configurations
    of the rule (rotations and translations) """
    rules = dict(in_rules)
    for left, right in in_rules.items():
        for config in all_configurations_of(left):
            rules[config] = right
    return rules


def translate_rule_to_matrix(rule):
    "translates string to a set of local coordinates of that block"
    return np.array([list(line) for line in rule.split('/')])


def translate_matrix_to_rule(in_matrix):
    return '/'.join(line for line in (''.join(c for c in line_list) for line_list in in_matrix))


def enhance(in_matrix):
    size = in_matrix.shape[0]
    cbs = 2 if size % 2 == 0 else 3 # current block size
    nbs = cbs + 1                   # new block size
    subblocks = size // cbs         # total subblocks per dimension


    if subblocks == 1:
        return expanded_rules[translate_matrix_to_rule(in_matrix)]

    enhanced = np.empty((subblocks*nbs, subblocks*nbs), dtype=str)
    for hor in range(subblocks):
        for ver in range(subblocks):
            block = in_matrix[cbs*hor:cbs*(hor+1), cbs*ver:cbs*(ver+1)]
            enhanced[nbs*hor:nbs*(hor+1), nbs*ver:nbs*(ver+1)] = expanded_rules[translate_matrix_to_rule(block)]

    return enhanced


def count_pixels(in_matrix):
    is_on = in_matrix == '#'
    return np.count_nonzero(is_on)



raw_rules = (line.split(' => ') for line in get_input('inputs/21'))

# a basic set of rules; from input
rules = {left: translate_rule_to_matrix(right) for left, right in raw_rules}

# an expanded set of rules, takes into acc. all configurations
expanded_rules = expand_rules(rules)

# start from here
current_state = translate_rule_to_matrix('.#./..#/###')

for count in range(1,19):
    current_state = enhance(current_state)
    if count == 5:
        part_1 = count_pixels(current_state)
    if count == 18:
        part_2 = count_pixels(current_state)

print_solutions(part_1, part_2)
# Part 1 solution is: 186
# Part 2 solution is: 3018423
