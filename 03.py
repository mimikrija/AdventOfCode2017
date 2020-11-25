def generate_coordinate(coordinates, dist, orientation_vector):
    coordinate = coordinates[-1]
    for _ in range(dist):
        coordinate = tuple(coordinate[i]+orientation_vector[i] for i in range(2))
        coordinates.append(coordinate)
    return coordinates

def manhattan_distance(coordinate):
    return sum(abs(p) for p in coordinate)

orientation_vectors = {
    1: (-1, 0),
    2: (0, -1),
    3: (1, 0),
    0: (0, 1)
}

# first three coordinates are special cases
locations = [(0,0),(1,0),(1,1)]

total_count = 325489
distance = 2
rotation = 1

# after that we always follow the pattern: 2 x (turn left, go n), where n = 2, 3, 4, ...
while len(locations) < total_count:
    for _ in range(2):
        locations = generate_coordinate(locations,distance,orientation_vectors[rotation%4])
        rotation +=1
    distance += 1

print(manhattan_distance(locations[total_count-1]))