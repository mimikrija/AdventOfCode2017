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

def solution(a, b, c):
    D = discriminant(a, b, c)
    if D < 0: # no real/finite solutions
        return False

    if a == 0: # not a quadratic equation
        if b !=0:
            solutions = [-c/b]
        else:
            return False
    else: # quadratic equation, two solutions
        solutions = ((-b + root_factor * sqrt(D))/(2*a) for root_factor in (-1, 1))

    return (sol for sol in solutions if sol >= 0)


def is_coliding(particle_one, particle_two):
    x_1, y_1, z_1 = particle_one.position
    x_2, y_2, z_2 = particle_two.position

    vx_1, vy_1, vz_1 = particle_one.velocity
    vx_2, vy_2, vz_2 = particle_two.velocity

    ax_1, ay_1, az_1 = particle_one.acceleration
    ax_2, ay_2, az_2 = particle_two.acceleration

    A_x = (ax_1-ax_2) / 2
    B_x = (ax_1-ax_2) /2 + vx_1 - vx_2
    C_x = x_1 - x_2

    A_y = (ay_1-ay_2) / 2
    B_y = (ay_1-ay_2) /2 + vy_1 - vy_2
    C_y = y_1 - y_2

    A_z = (az_1-az_2) / 2
    B_z = (az_1-az_2) /2 + vz_1 - vz_2
    C_z = z_1 - z_2
    
    all_solutions = [solution(A_x, B_x, C_x), solution(A_y, B_y, C_y), solution(A_z, B_z, C_z)]
    if not all_solutions:
        return False

    if any(not sol for sol in all_solutions):
        return False

    # if any(not sol for sol in (solution(A_x, B_x, C_x), solution(A_y, B_y, C_y), solution(A_z, B_z, C_z)) ):
    #     return False
    else:
        all_solutions = [*solution(A_x, B_x, C_x), *solution(A_y, B_y, C_y), *solution(A_z, B_z, C_z)]
        #all_solutions = [*sol for sol in all_solutions]
        if not all_solutions:
            return False
        count_solutions = Counter(all_solutions).most_common()
        if count_solutions[0][1] == 3:
            return count_solutions[0][0] # colision time


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



remaining = set(particle_data)
colliding = set()
times = []
collisions = {}
for one, two in combinations(particle_data, 2):
    time = is_coliding(one, two)
    if time:
        if time in collisions:
            collisions[time].append(one)
            collisions[time].append(two)
        else:
            collisions[time] = [one, two]


removed_so_far = set()
for time, members in sorted(collisions.items()):
    remaining -= set(members)

remaining_particles = len(remaining)


print_solutions(closest, remaining_particles)
# Part 1 solution is: 170
# Part 2 solution is: 571
