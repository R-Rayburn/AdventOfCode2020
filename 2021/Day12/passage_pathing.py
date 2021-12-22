print('Passage Pathing')

with open('data.txt', 'r') as input_data:
    cave_map = [d for d in input_data.read().split('\n') if d]
with open('test_one.txt', 'r') as test:
    test_one_cave_map = [t for t in test.read().split('\n') if t]
with open('test_two.txt', 'r') as test:
    test_two_cave_map = [t for t in test.read().split('\n') if t]
with open('test_three.txt', 'r') as test:
    test_three_cave_map = [t for t in test.read().split('\n') if t]


def draw_map(cm):
    cave_system = {}
    for cave_path in cm:
        c1, c2 = cave_path.split('-')
        if c2 != 'start' and c1 != 'end':
            if c1 in cave_system.keys():
                cave_system[c1].append(c2)
            else:
                cave_system[c1] = [c2]
        if c1 != 'start' and c2 != 'end':
            if c2 in cave_system.keys():
                cave_system[c2].append(c1)
            else:
                cave_system[c2] = [c1]
    return cave_system


def find_paths(path, cave_system, saved_paths):
    if path[-1] == 'end':
        saved_paths.append(path)
        return
    for value in cave_system[path[-1]]:
        if value != 'end' and all([x.islower() for x in value]) and value in path:
            continue
        find_paths(path + [value], cave_system, saved_paths)


def get_path_count(m):
    drawn_map = draw_map(m)
    paths = []
    find_paths(['start'], drawn_map, paths)
    return len(paths)


print('Part 1')
print(f'Test 1: {get_path_count(test_one_cave_map)}')
print(f'Test 2: {get_path_count(test_two_cave_map)}')
print(f'Test 3: {get_path_count(test_three_cave_map)}')
print(f'Data: {get_path_count(cave_map)}')


def has_duplicate_lowers(path):
    lowers = [p for p in path if all([x.islower() for x in p]) and p != 'end']
    lowers_set = set(lowers)
    return len(lowers) != len(lowers_set)


def find_paths_p2(path, cave_system, saved_paths):
    if path[-1] == 'end':
        saved_paths.append(path)
        return
    for value in cave_system[path[-1]]:
        if value != 'end' and all([x.islower() for x in value]) and value in path and has_duplicate_lowers(path[1:]):
            continue
        find_paths_p2(path + [value], cave_system, saved_paths)


def get_path_count_p2(m):
    drawn_map = draw_map(m)
    paths = []
    find_paths_p2(['start'], drawn_map, paths)
    return len(paths)


print('Part 2')
print(f'Test 1: {get_path_count_p2(test_one_cave_map)}')
print(f'Test 2: {get_path_count_p2(test_two_cave_map)}')
print(f'Test 3: {get_path_count_p2(test_three_cave_map)}')
print(f'Data: {get_path_count_p2(cave_map)}')
