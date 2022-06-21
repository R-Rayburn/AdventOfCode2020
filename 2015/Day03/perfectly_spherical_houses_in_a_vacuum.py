print('Perfectly Spherical houses in a vacuum')

with open('data.txt', 'r') as file:
    radio_moves = file.read()


def add_tuples(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


def log_present_location(moves):
    location = (0, 0)
    visited = {location: 1}
    for move in moves:
        if move == '^':
            location = add_tuples(location, (1, 0))
        elif move == '>':
            location = add_tuples(location, (0, 1))
        elif move == 'v':
            location = add_tuples(location, (-1, 0))
        elif move == '<':
            location = add_tuples(location, (0, -1))
        visited[location] = visited.get(location, 0) + 1
    return visited


def get_number_of_visited_houses(data):
    visited_houses = log_present_location(data)
    return len(visited_houses.keys())


print('Part 1')
print(f'Test 1: {get_number_of_visited_houses(">")}')  # 2
print(f'Test 2: {get_number_of_visited_houses("^>v<")}')  # 4
print(f'Test 3: {get_number_of_visited_houses("^v^v^v^v^v")}')  # 2
print(f'Data: {get_number_of_visited_houses(radio_moves)}')


def get_combined_number_of_visited_houses(data):
    santa_visited = log_present_location(data[0::2])
    robo_santa_visited = log_present_location(data[1::2])
    santa_visited.update(robo_santa_visited)
    return len(santa_visited.keys())


print('Part 2')
print(f'Test 1: {get_combined_number_of_visited_houses("^v")}')  # 2
print(f'Test 2: {get_combined_number_of_visited_houses("^>v<")}')  # 4
print(f'Test 3: {get_combined_number_of_visited_houses("^v^v^v^v^v")}')  # 2
print(f'Data: {get_combined_number_of_visited_houses(radio_moves)}')
