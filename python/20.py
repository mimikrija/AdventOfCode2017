# Day 20: Particle Swarm

from santas_little_helpers import *
import re
from collections import namedtuple
from math import sqrt
from collections import Counter
from itertools import combinations

def magnitude(in_named):
    return sqrt(sum(num**2 for num in in_named))

def discriminant(a, b, c):
    return b**2 - 4*a*c


def solve_quadratic(a, b, c):
    D = discriminant(a, b, c)

    if D < 0: # no real/finite solutions
        return [None]

    if a == 0: # not a quadratic equation
        try:
            return [-c/b]
        except:
            return [None]

    # quadratic equation, one/two solutions
    # using set here in case D == 0 and we get two identical solutions
    return list({(-b + root_factor * sqrt(D))/(2*a) for root_factor in (-1, 1)})


def ABC(first_component, second_component):
    C, B, A = (one-two for one, two in zip(first_component, second_component))

    A /= 2
    B += A

    return A, B, C


def solve_per_component(particle_one, particle_two):
    solutions = []
    # this gives us tuples of position, velocity, and acceleration
    # of both particles per component X, Y, Z
    for xva_component in zip(zip(*particle_one), zip(*particle_two)):
        solutions += solve_quadratic(*ABC(*xva_component))

    return solutions


def get_colision_time(particle_one, particle_two):
    valid_solutions = (sol for sol in solve_per_component(particle_one, particle_two)
                                        if sol and sol >= 0)

    count_solutions = Counter(valid_solutions).most_common()
    try:
        if count_solutions[0][1] == 3:
        # all components colide at the same tame
            return count_solutions[0][0]
    except:
        return None


def generate_collisions(in_data):
    collisions = {}
    for one, two in combinations(in_data, 2):
        time = get_colision_time(one, two)
        if time:
            collisions[time] = collisions.get(time, set()) | {one, two}

    return collisions


def live_after_colliding(in_data):
    already_destroyed = set()
    alive = set(in_data)
    for time, particles in sorted(generate_collisions(in_data).items()):
        if len(particles & already_destroyed) == 1:
            print('this one stays alive')
            continue
        else:
            alive -= particles
            already_destroyed |= particles

    return len(alive)



ParticleData = namedtuple('ParticleData', ['position', 'velocity', 'acceleration'])

input_pattern = re.compile(r'p=<(-*\d+,-*\d+,-*\d+)>, v=<(-*\d+,-*\d+,-*\d+)>, a=<(-*\d+,-*\d+,-*\d+)>')

particle_data = []
for line in get_input('inputs/20'):
    position, velocity, acceleration = (tuple(map(int, data.split(',')))
                                        for data in re.match(input_pattern, line).groups())
    particle = ParticleData(position, velocity, acceleration)
    particle_data.append(particle)

# in the "long run", the closest particle is the one with smallest acceleration
closest = particle_data.index(min(particle_data, key=lambda arg: magnitude(arg.acceleration)))

remaining_particles = live_after_colliding(particle_data)


print_solutions(closest, remaining_particles)
# Part 1 solution is: 170
# Part 2 solution is: 571
