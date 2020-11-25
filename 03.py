def manhattan_distance(coordinate):
    return sum(abs(p) for p in coordinate)

def is_neighbor(coordinate,potential_neighbor):
    return abs(coordinate[0]-potential_neighbor[0]) <= 1 and abs(coordinate[1]-potential_neighbor[1]) <= 1

orientation_vectors = {
    1: (-1, 0),
    2: (0, -1),
    3: (1, 0),
    0: (0, 1)
}
# puzzle input
total_count = 325489

# first three coordinates are special cases
locations = [(0,0),(1,0),(1,1)]
values = [1,1,2]
distance = 2
rotation = 1

solution_2 = None

# after that we always follow the pattern: 2 x (turn left, go distance), where distance = 2, 3, 4, ...
while len(locations) < total_count:
    for _ in range(2):
        coordinate = locations[-1]
        for _ in range(distance):
            coordinate = tuple(coordinate[i]+orientation_vectors[rotation%4][i] for i in range(2))
            # part 2: sum the values of neighbouring coordinates
            value = 0
            if solution_2 == None:
                # check for potential neighbors in all locations travelled so far
                for neighbor in locations:
                    if is_neighbor(coordinate,neighbor):
                        # for each neighbor add up their values
                        value += values[locations.index(neighbor)]
                values.append(value)
                if value > total_count:
                    solution_2 = value
            # end of part 2
            locations.append(coordinate)
        rotation +=1 # turn left again / increment rotation
    distance += 1 # increase overall distance by one because we are in the new spiral now

print ("Part 1 solution is: ", manhattan_distance(locations[total_count-1]))
# Part 1 solution is:  552
print ("Part 2 solution is: ", solution_2)
# Part 2 solution is:  330785
