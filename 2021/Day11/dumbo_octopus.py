print('Dumbo Octopus')

with open('data.txt', 'r') as input_data:
    dumbo_octopi_data = [[int(o) for o in d] for d in input_data.read().split('\n') if d]
with open('test.txt', 'r') as test:
    test_dumbo_octopi_data = [[int(o) for o in t] for t in test.read().split('\n') if t]


def increment_flashes(octopi, row, col):
    if row < 0 or col < 0 or row >= len(octopi) or col >= len(octopi[0]) or octopi[row][col] == -1:
        return
    elif octopi[row][col] == 9:
        octopi[row][col] = -1
        increment_flashes(octopi, row + 1, col)
        increment_flashes(octopi, row + 1, col + 1)
        increment_flashes(octopi, row + 1, col - 1)
        increment_flashes(octopi, row, col + 1)
        increment_flashes(octopi, row, col - 1)
        increment_flashes(octopi, row - 1, col)
        increment_flashes(octopi, row - 1, col + 1)
        increment_flashes(octopi, row - 1, col - 1)
    else:
        octopi[row][col] += 1


def get_flash_count(octopi):
    return len([col for row in octopi for col in row if col == -1])


def reset_octopi(octopi):
    for row in range(len(octopi)):
        for col in range(len(octopi[row])):
            if octopi[row][col] == -1:
                octopi[row][col] = 0


def print_octopi(octopi, step):
    print(f'--- After Step {step} ---')
    for i in range(len(octopi)):
        print(''.join([str(x) for x in octopi[i]]))
    print('\n')


def calculate_flashes(octopi, steps):
    total_flashes = 0
    for i in range(steps):
        for row in range(len(octopi)):
            for col in range(len(octopi[row])):
                increment_flashes(octopi, row, col)
        total_flashes += get_flash_count(octopi)
        reset_octopi(octopi)
        # print_octopi(octopi, i+1)
    return total_flashes


print('Part 1')
print(f'Test: {calculate_flashes(test_dumbo_octopi_data, 100)}')
print(f'Data: {calculate_flashes(dumbo_octopi_data, 100)}')


def all_are_flashing(octopi):
    return all([True if col == 0 else False for row in octopi for col in row])


def find_step_where_all_flash(octopi):
    step = 0
    while not all_are_flashing(octopi):
        for row in range(len(octopi)):
            for col in range(len(octopi[row])):
                increment_flashes(octopi, row, col)
        step += 1
        reset_octopi(octopi)
    return step


# Since I am altering data by reference, need to add 100 to result
print('Part 2')
print(f'Test: {find_step_where_all_flash(test_dumbo_octopi_data) + 100}')
print(f'Data: {find_step_where_all_flash(dumbo_octopi_data) + 100}')
