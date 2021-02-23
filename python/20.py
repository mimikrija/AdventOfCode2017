# Day 20: Particle Swarm

from santas_little_helpers import *
from re import findall
from collections import namedtuple
from math import sqrt
from collections import Counter
from itertools import product

def magnitude(in_named):
    return sqrt(in_named[0]**2 + in_named[1]**2 + in_named[2]**2)

def discriminant(a, b, c):
    return b**2 - 4*a*c

def solution(a, b, c):
    D = discriminant(a, b, c)
    if a == 0 or D < 0: # no real/finite solutions
        return False

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

    if any(not sol for sol in all_solutions):
        return False

    # if any(not sol for sol in (solution(A_x, B_x, C_x), solution(A_y, B_y, C_y), solution(A_z, B_z, C_z)) ):
    #     return False
    else:
        all_solutions = [*solution(A_x, B_x, C_x), *solution(A_y, B_y, C_y), *solution(A_z, B_z, C_z)]
        #all_solutions = [*sol for sol in all_solutions]
        count_solutions = Counter(all_solutions).most_common()
        if count_solutions[0][1] == 3:
            return count_solutions[0][0] # colision time



ParticleData = namedtuple('ParticleData', ['position', 'velocity', 'acceleration'])
Position = namedtuple('Position', ['x', 'y', 'z'])
Velocity = namedtuple('Velocity', ['x', 'y', 'z'])
Acceleration = namedtuple('Acceleration', ['x', 'y', 'z'])

particle_raw_data = [list(map(int, findall(r'[-]*\d+', line))) for line in get_input('inputs/20')]
particle_data = []
for data in particle_raw_data:
    position = tuple(data[:3])
    velocity = tuple(data[3:6])
    acceleration = tuple(data[6:])
    particle_data.append(ParticleData(position, velocity, acceleration))


# in the "long run", the closest particle is the one with smallest acceleration
closest = particle_data.index(min(particle_data, key=lambda arg: magnitude(arg.acceleration)))
print_solutions(closest)


remaining = set(particle_data)
colliding = set()
times = []
collisions = {}
for one, two in product(particle_data, repeat=2):
    time = is_coliding(one, two)
    if time:
        if time in collisions:
            collisions[time].append(one)
            collisions[time].append(two)
        else:
            collisions[time] = [one, two]
            #colliding.add(one)
            #colliding.add(two)

removed_so_far = set()
for time, members in sorted(collisions.items()):
    print(time, len(set(members)))
    if len(removed_so_far & set(members)) == 1:
        print('helo')
        continue
    removed_so_far |= set(members)
    remaining -= set(members)
    #print(time, len(members), len(set(members)))
    #print(len(remaining))

print(len(remaining)) # 575 to high
