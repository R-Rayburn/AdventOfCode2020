print('Hydrothermal Venture')

with open('data.txt', 'r') as data:
    points = [d for d in data.read().split('\n') if d]
with open('test.txt', 'r') as test:
    test_points = [t for t in test.read().split('\n') if t]


def get_points_between(point1, point2):
    list_of_points = []
    if point1[0] == point2[0]:
        min_point = min(int(point1[1]), int(point2[1]))
        max_point = max(int(point1[1]), int(point2[1]))
        ys = [y for y in range(min_point, max_point + 1)]
        list_of_points = [(point1[0], str(y)) for y in ys]
    elif point1[1] == point2[1]:
        min_point = min(int(point1[0]), int(point2[0]))
        max_point = max(int(point1[0]), int(point2[0]))
        xs = [x for x in range(min_point, max_point + 1)]
        list_of_points = [(str(x), point1[1]) for x in xs]
    return list_of_points


def format_data(lines):
    formatted_points = []
    for point1, point2 in [ps.split(' -> ') for ps in lines]:
        x1, y1 = point1.split(',')
        x2, y2 = point2.split(',')
        formatted_points.append(((x1, y1), (x2, y2)))
    return formatted_points


def get_diagonal_points(point1, point2):
    diagonal_points = []
    x1 = int(point1[0])
    y1 = int(point1[1])
    x2 = int(point2[0])
    y2 = int(point2[1])
    if x1 != x2 and y1 != y2:
        xs = []
        if x1 < x2:
            xs += [str(x) for x in range(x1, x2 + 1)]
        elif x1 > x2:
            xs += [str(x) for x in range(x1, x2 - 1, -1)]

        ys = []
        if y1 < y2:
            ys += [str(y) for y in range(y1, y2 + 1)]
        elif y1 > y2:
            ys += [str(y) for y in range(y1, y2 - 1, -1)]

        print(f'xs: {xs}')
        print(f'ys: {ys}')
        print(point1)
        print(point2)
        for i in range(len(xs)):
            diagonal_points.append((xs[i], ys[i]))
        # Get diagonal values
        #   create points from point1 to point2 diagonally
        #   this will mean you will need to get ranges between x1, x2 and y1, y2
        #   and loop through the loop to calculate values.
    return diagonal_points


def set_all_points(start_points, include_diagonal=False):
    all_points = {}
    for ps in format_data(start_points):
        point1 = ps[0]
        point2 = ps[1]
        points_between = get_points_between(point1, point2)
        # = Part 2
        if include_diagonal:
            diagonal_points = get_diagonal_points(point1, point2)
            if len(diagonal_points) > 0:
                points_between += diagonal_points
        # =
        for p in points_between:
            if p in all_points.keys():
                all_points[p] += 1
            else:
                all_points[p] = 1
    return all_points


def find_dangerous_areas(start_points, include_diagonal=False):
    all_points = {}
    if include_diagonal:
        all_points = set_all_points(start_points, True)
    else:
        all_points = set_all_points(start_points)
    return len([point for point in all_points if all_points[point] > 1])


print('Part 1')
print(f'Test: {find_dangerous_areas(test_points)}')
print(f'Data: {find_dangerous_areas(points)}')
print('Part 2')
print(f'Test: {find_dangerous_areas(test_points, True)}')
print(f'Test: {find_dangerous_areas(points, True)}')
