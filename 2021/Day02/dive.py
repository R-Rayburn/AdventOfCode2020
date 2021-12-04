print('Dive!')

with open('data.txt', 'r') as data:
    data_numbers = [x for x in data.read().split('\n') if x]
with open('test.txt', 'r') as test:
    test_numbers = [x for x in test.read().split('\n') if x]


def add_value(direction, mag):
    if direction == 'forward':
        return mag, 0
    elif direction == 'up':
        return 0, -mag
    elif direction == 'down':
        return 0, mag
    else:
        return 0, 0


def finding_position(file_info):
    position = (0, 0)
    for direction in file_info:
        d, m = direction.split(' ')
        position = tuple(map(sum, zip(position, add_value(d, int(m)))))
    return position[0] * position[1]


print('Part 1:')
print(f'Test Answer: {finding_position(test_numbers)}')
print(f'Data Answer: {finding_position(data_numbers)}')


def configure_aim(file_info):
    position = (0, 0)
    aim = 0
    for info in file_info:
        direction, mag = info.split(' ')
        if direction == 'up':
            aim -= int(mag)
        elif direction == 'down':
            aim += int(mag)
        else:
            position = (int(mag) + position[0], position[1] + (aim * int(mag)))
    return position[0] * position[1]


print('Part2:')
print(f'Test Answer: {configure_aim(test_numbers)}')  # should be 900
print(f'Data Answer: {configure_aim(data_numbers)}')
