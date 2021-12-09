print('The Treachery of Whales')

with open('data.txt', 'r') as input_data:
    crab_sub_position = [int(d) for d in input_data.read().split(',') if d]
with open('test.txt', 'r') as test:
    test_position = [int(t) for t in test.read().split(',') if t]


def find_fuel_consumption(sub_positions):
    fuel_consumption = []
    min_position = min(sub_positions)
    max_position = max(sub_positions)
    position_counts = {position: 0 for position in range(min_position, max_position + 1)}
    for position in sub_positions:
        position_counts[position] += 1
    for position in position_counts:
        fuel_consumption.append(sum([abs(position-p) * position_counts[p] for p in position_counts]))
    return min(fuel_consumption)


print('Part 1')
print(f'Test: {find_fuel_consumption(test_position)}')
print(f'Data: {find_fuel_consumption(crab_sub_position)}')


def find_correct_fuel_consumption(sub_positions):
    fuel_consumption = []
    min_position = min(sub_positions)
    max_position = max(sub_positions)
    position_counts = {position: 0 for position in range(min_position, max_position + 1)}
    for position in sub_positions:
        position_counts[position] += 1
    for position in position_counts:
        fuel_consumption.append(sum([sum([x for x in range(1, abs(position - p) + 1)]) * position_counts[p] for p in position_counts]))
    return min(fuel_consumption)


print('Part 2')
print(f'Test: {find_correct_fuel_consumption(test_position)}')
print(f'Data: {find_correct_fuel_consumption(crab_sub_position)}')
