import numpy as np

with open('data.txt', 'r') as f:
    prior_state = [list(x) for x in f.read().split('\n') if x]


def check_for_active(grid, z, x, y):
    if grid[z][x][y] == '#':
        return 1
    return 0


def init_grid(grid):
    return [np.array(grid)]


def add_layer(grid):
    column_to_be_added = np.array(['.']*len(grid))
    grid = np.column_stack((column_to_be_added, grid, column_to_be_added))
    row_to_be_added = np.array(['.']*len(grid[0]))
    grid = np.row_stack((row_to_be_added, grid, row_to_be_added))
    return grid


def create_new_stack(r, c):
    return np.full((r, c), '.')


# chaos = True
new_state = init_grid(prior_state)
prior_state = init_grid(prior_state)


def increase_grid(grid):
    for i in range(len(grid)):
        state = add_layer(grid[i])
        np.resize(grid[i], (len(grid[i]) + 1, len(grid[i][0]) + 1))
        grid[i] = state
    grid.insert(0, create_new_stack(len(grid[0]), len(grid[0][0])))
    grid.append(create_new_stack(len(grid[0]), len(grid[0][0])))


increase_grid(new_state)
increase_grid(prior_state)

for cycle in range(7):
    for z in range(len(new_state)):
        for x in range(len(new_state[z])):
            for y in range(len(new_state[z][x])):
                adj_box_active = 0

                # adj_box_active += check_for_active(prior_state, z, x, y + 1)
                # adj_box_active += check_for_active(prior_state, z, x, y - 1)
                # adj_box_active += check_for_active(prior_state, z, x + 1, y)
                # adj_box_active += check_for_active(prior_state, z, x - 1, y)
                # adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                # adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                # adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                # adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                # adj_box_active += check_for_active(prior_state, z + 1, x, y)
                # adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                # adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                # adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                # adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                # adj_box_active += check_for_active(prior_state, z + 1, x + 1, y + 1)
                # adj_box_active += check_for_active(prior_state, z + 1, x + 1, y - 1)
                # adj_box_active += check_for_active(prior_state, z + 1, x - 1, y + 1)
                # adj_box_active += check_for_active(prior_state, z + 1, x - 1, y - 1)
                # adj_box_active += check_for_active(prior_state, z - 1, x, y)
                # adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                # adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                # adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                # adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                # adj_box_active += check_for_active(prior_state, z - 1, x + 1, y + 1)
                # adj_box_active += check_for_active(prior_state, z - 1, x + 1, y - 1)
                # adj_box_active += check_for_active(prior_state, z - 1, x - 1, y + 1)
                # adj_box_active += check_for_active(prior_state, z - 1, x - 1, y - 1)

                if z == 0:
                    if x == 0:
                        if y == 0:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y + 1)
                        elif y == len(new_state[z][x]) - 1:
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y - 1)
                        else:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y - 1)
                    elif x == len(new_state[z]) - 1:
                        if y == 0:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y + 1)
                        elif y == len(new_state[z][x]) - 1:
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y - 1)
                        else:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y - 1)
                    else:
                        if y == 0:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y + 1)
                        elif y == len(new_state[z][x]) - 1:
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y - 1)
                        else:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y - 1)
                elif z == len(new_state) - 1:
                    if x == 0:
                        if y == 0:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y + 1)
                        elif y == len(new_state[z][x]) - 1:
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y - 1)
                        else:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y - 1)
                    elif x == len(new_state[z]) - 1:
                        if y == 0:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y + 1)
                        elif y == len(new_state[z][x]) - 1:
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y - 1)
                        else:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y - 1)
                    else:
                        if y == 0:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y + 1)
                        elif y == len(new_state[z][x]) - 1:
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y - 1)
                        else:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y - 1)
                else:
                    if x == 0:
                        if y == 0:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y + 1)
                        elif y == len(new_state[z][x]) - 1:
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y - 1)
                        else:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y - 1)
                    elif x == len(new_state[z]) - 1:
                        if y == 0:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y + 1)
                        elif y == len(new_state[z][x]) - 1:
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y - 1)
                        else:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y - 1)
                    else:
                        if y == 0:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y + 1)
                        elif y == len(new_state[z][x]) - 1:
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y - 1)
                        else:
                            adj_box_active += check_for_active(prior_state, z, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z + 1, x - 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x + 1, y - 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y + 1)
                            adj_box_active += check_for_active(prior_state, z - 1, x - 1, y - 1)

                if prior_state[z][x][y] == '#' and adj_box_active not in range(2,4):
                    new_state[z][x][y] = '.'
                elif prior_state[z][x][y] == '.' and adj_box_active == 3:
                    new_state[z][x][y] = '#'
                else:
                    new_state[z][x][y] = prior_state[z][x][y]
            print(new_state[z][x])
    increase_grid(new_state)
    increase_grid(prior_state)
    temp = prior_state[:]
    prior_state = new_state[:]
    new_state = temp[:]

hash_count = 0
for z in new_state:
    for x in z:
        for y in x:
            if y == '#':
                hash_count += 1
print(hash_count)
