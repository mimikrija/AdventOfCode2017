# Day 21: Fractal Art

from santas_little_helpers import *
from itertools import chain

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


def translate_rule_to_set(rule):
    "translates string to a set of local coordinates of that block"
    return {(row, column) for row, line in enumerate(rule.split('/'))
            for column, c in enumerate(line)
            if c == '#'}


def translate_set_to_rule(coords, size):
    out_rule = ''
    for row in range(size):
        line = ['.']*size
        for column in range(size):
            if (row, column) in coords:
                line[column] = '#'
        out_rule += ''.join(line) + '/'
    return out_rule[:-1]


def local_to_global(in_matrix, sub_block_size):
    size = len(in_matrix)
    out_global = set()
    for x in range(size):
        for y in range(size):
            out_global.add


def global_to_local(in_global, sub_block_size, blocks):
    max_hor = max(in_global)[0]
    max_vert = max(in_global,key=lamda x: x[1])[0]
    out_matrix = []
    for row in blocks:
        for column in blocks:
            out_matrix.append({(x, y) for (x, y) in in_global 
            if column <= x < column + sub_block_size and row <= y < row + sub_block_size})
    return out_matrix

def enhance(in_matrix, sub_block_size):
    blocks_hor = len(in_matrix)
    block_vert = len(in_matrix[0])
    block_size = len(in_matrix[0][0].split('/')[0])
    size = blocks_hor * sub_block_size
    if block_size == 3:
        # enhance blocks immediatelly
        out_matrix = []
        for row, row_block in enumerate(in_matrix):
            new_line = [' ']*blocks_hor
            for column, block in enumerate(row_block):
                new_line[column] = expanded_rules[block]
            out_matrix.append(new_line)
        enhanced_block_size = 4


    else:
        divisions = next(div for div, rest in (divmod(size, n) for n in {2,3}) if rest == 0)


    
    print(block_vert, blocks_hor, size)
    return out_matrix, enhanced_block_size




raw_rules = (line.split(' => ') for line in get_input('inputs/21-ex'))

# a basic set of rules; from input
rules = {left: translate_to_set(right) for left, right in raw_rules}

# an expanded set of rules, takes into acc. all configurations
expanded_rules = expand_rules(rules)

#print(list(expanded_rules.keys()))

start = [['.#./..#/###']]

#print(all_configurations_of('.#./..#/#..'))

print(enhance(start, 3))
