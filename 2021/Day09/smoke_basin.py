import math

print('Smoke Basin')

with open('data.txt', 'r') as input_data:
    heat_map = [[int(i) for i in d] for d in input_data.read().split('\n') if d]
with open('test.txt', 'r') as test:
    test_heat_map = [[int(i) for i in t] for t in test.read().split('\n') if t]


def less_than_right(h_map, row, col):
    return h_map[row][col] < h_map[row][col + 1]


def less_than_left(h_map, row, col):
    return h_map[row][col] < h_map[row][col - 1]


def less_than_bottom(h_map, row, col):
    return h_map[row][col] < h_map[row + 1][col]


def less_than_top(h_map, row, col):
    return h_map[row][col] < h_map[row - 1][col]


def is_lowest_top_left(h_map, row, col):
    return row == 0\
           and col == 0\
           and less_than_bottom(h_map, row, col)\
           and less_than_right(h_map, row, col)


def is_lowest_top_right(h_map, row, col):
    return row == 0\
           and col == len(h_map[row]) - 1\
           and less_than_bottom(h_map, row, col)\
           and less_than_left(h_map, row, col)


def is_lowest_bottom_left(h_map, row, col):
    return row == len(h_map) - 1\
           and col == 0\
           and less_than_top(h_map, row, col)\
           and less_than_right(h_map, row, col)


def is_lowest_bottom_right(h_map, row, col):
    return row == len(h_map) - 1\
           and col == len(h_map[row]) - 1\
           and less_than_top(h_map, row, col)\
           and less_than_left(h_map, row, col)


def is_lowest_top(h_map, row, col):
    return row == 0 \
           and col != 0 \
           and col != len(h_map[row]) - 1 \
           and less_than_left(h_map, row, col)\
           and less_than_bottom(h_map, row, col)\
           and less_than_right(h_map, row, col)


def is_lowest_right(h_map, row, col):
    return col == len(h_map[row]) - 1\
           and row != 0\
           and row != len(h_map) - 1\
           and less_than_top(h_map, row, col)\
           and less_than_bottom(h_map, row, col)\
           and less_than_left(h_map, row, col)


def is_lowest_bottom(h_map, row, col):
    return row == len(h_map) - 1 \
           and col != 0 \
           and col != len(h_map[row]) - 1 \
           and less_than_top(h_map, row, col)\
           and less_than_left(h_map, row, col)\
           and less_than_right(h_map, row, col)


def is_lowest_left(h_map, row, col):
    return col == 0 \
           and row != 0 \
           and row != len(h_map) - 1 \
           and less_than_top(h_map, row, col)\
           and less_than_bottom(h_map, row, col)\
           and less_than_right(h_map, row, col)


def is_lowest_center(h_map, row, col):
    return row != 0\
           and row != len(h_map) - 1\
           and col != 0\
           and col != len(h_map[row]) - 1\
           and less_than_top(h_map, row, col)\
           and less_than_bottom(h_map, row, col)\
           and less_than_left(h_map, row, col)\
           and less_than_right(h_map, row, col)


def find_low_points(h_map):
    low_points = []
    for i in range(len(h_map)):
        for j in range(len(h_map[i])):
            if is_lowest_top_left(h_map, i, j):
                low_points.append(h_map[i][j])
            elif is_lowest_top_right(h_map, i, j):
                low_points.append(h_map[i][j])
            elif is_lowest_bottom_left(h_map, i, j):
                low_points.append(h_map[i][j])
            elif is_lowest_bottom_right(h_map, i, j):
                low_points.append(h_map[i][j])
            elif is_lowest_top(h_map, i, j):
                low_points.append(h_map[i][j])
            elif is_lowest_bottom(h_map, i, j):
                low_points.append(h_map[i][j])
            elif is_lowest_left(h_map, i, j):
                low_points.append(h_map[i][j])
            elif is_lowest_right(h_map, i, j):
                low_points.append(h_map[i][j])
            elif is_lowest_center(h_map, i, j):
                low_points.append(h_map[i][j])
    return sum([x+1 for x in low_points])


print('Part 1')
print(f'Test: {find_low_points(test_heat_map)}')
print(f'Data: {find_low_points(heat_map)}')


basins = []


def count_basin(row, col, h_map):
    if row < 0 or row >= len(h_map) or col < 0 or col >= len(h_map[row]) or h_map[row][col] == 9 or h_map[row][col] == -1:
        return
    h_map[row][col] = -1
    basins[len(basins)-1] += 1
    count_basin(row+1, col, h_map)
    count_basin(row-1, col, h_map)
    count_basin(row, col+1, h_map)
    count_basin(row, col-1, h_map)


def calculate_answer(h_map):
    for i in range(len(h_map)):
        for j in range(len(h_map[i])):
            basins.append(0)
            count_basin(i, j, h_map)
    return math.prod(sorted(basins, reverse=True)[:3])


print('Part 2')
print(f'Test: {calculate_answer(test_heat_map)}')
print(f'Data: {calculate_answer(heat_map)}')
