def find_neighbor_dimensions(xyzw):
    my_x = xyzw[0]
    my_y = xyzw[1]
    my_z = xyzw[2]
    my_w = xyzw[3]
    neighbors = []
    for xi in range(my_x - 1, my_x + 2):
        for yi in range(my_y - 1, my_y + 2):
            for zi in range(my_z - 1, my_z + 2):
                for wi in range(my_w - 1, my_w + 2):
                    neighbors.append((xi, yi, zi, wi))
    neighbors.remove((my_x, my_y, my_z, my_w))
    return neighbors


def update_dimensions(pocket_dimensions):
    neighbor_counts = {}
    for region in pocket_dimensions:
        if pocket_dimensions[region] == '#':
            neighbors = find_neighbor_dimensions(region)
            for neighbor in neighbors:
                try:
                    neighbor_counts[neighbor] += 1
                except KeyError:
                    neighbor_counts[neighbor] = 1
    conway_cubes = {}
    active_count = 0
    for counts in neighbor_counts:
        try:
            current_state = pocket_dimensions[counts]
        except KeyError:
            current_state = '.'

        if current_state == '#' and neighbor_counts[counts] not in range(2, 4):
            conway_cubes[counts] = '.'
        elif current_state == '.' and neighbor_counts[counts] == 3:
            conway_cubes[counts] = '#'
        else:
            conway_cubes[counts] = current_state

        if conway_cubes[counts] == '#':
            active_count += 1

    return conway_cubes, active_count


with open('data.txt', 'r') as f:
    initial_state = [list(x) for x in f.read().split('\n') if x]

pocket_dim = {}
counter = 0
for x in range(len(initial_state)):
    for y in range(len(initial_state[x])):
        pocket_dim[(x, y, 0, 0)] = initial_state[x][y]

for cycle in range(6):
    pocket_dim, counter = update_dimensions(pocket_dim)

print(counter)
