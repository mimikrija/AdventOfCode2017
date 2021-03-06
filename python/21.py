# Day 21: Fractal Art

from santas_little_helpers import *

def all_configurations_of(in_rule):

    def flip_horizontal(in_rule):
        rows = in_rule.split('/')
        return '/'.join(rows[::-1])

    def flip_both(in_rule):
        rows = [row[::-1] for row in flip_horizontal(in_rule).split('/')]
        return '/'.join(rows)

    config = str(in_rule)
    configs = {config}

    for _ in range(4):
        config = flip_both(config)
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


def translate_to_set(rule):
    "translates string to a set of local coordinates of that block"
    return {(row, column) for row, line in enumerate(rule.split('/'))
            for column, c in enumerate(line)
            if c == '#'}



raw_rules = (line.split(' => ') for line in get_input('inputs/21'))

# a basic set of rules; from input
rules = {left: translate_to_set(right) for left, right in raw_rules}

# an expanded set of rules, takes into acc. all configurations
expanded_rules = expand_rules(rules)

