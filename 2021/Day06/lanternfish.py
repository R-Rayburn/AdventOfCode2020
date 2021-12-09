print('Lanternfish')

with open('data.txt', 'r') as input_data:
    initial_state = [d for d in input_data.read().split('\n') if d]
with open('test.txt', 'r') as test:
    test_state = [t for t in test.read().split('\n') if t]


def calculate_80_day_incubation(data):
    fish = [int(x) for x in data.split(',')]
    for i in range(80):
        fish_to_add = len([f for f in fish if f == 0])
        fish = [f - 1 if f - 1 > -1 else 6 for f in fish]
        fish += [8 for _ in range(fish_to_add)]
    return len(fish)


print('Part 1')
print(f'Test: {calculate_80_day_incubation(test_state[0])}')
print(f'Data: {calculate_80_day_incubation(initial_state[0])}')


def calculate_infinite_incubation(data, days):
    # Use dictionary to contain counts and update counts
    fish = {n: 0 for n in range(9)}
    for d in data.split(','):
        fish[int(d)] += 1
    for _ in range(days):
        fish[-1] = fish[0]
        fish[0] = fish[1]
        fish[1] = fish[2]
        fish[2] = fish[3]
        fish[3] = fish[4]
        fish[4] = fish[5]
        fish[5] = fish[6]
        fish[6] = fish[7] + fish[-1]
        fish[7] = fish[8]
        fish[8] = fish[-1]
    return sum([age for age in fish.values()]) - fish[-1]


print('Part 2')
print(f'Test: {calculate_infinite_incubation(test_state[0], 256)}')
print(f'Data: {calculate_infinite_incubation(initial_state[0], 256)}')
