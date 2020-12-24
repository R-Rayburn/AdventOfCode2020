test_data = list(map(int, '389125467'))
data = list(map(int, '215694783'))
final_move = 100


def play_part_1(cups, move):
    if move > final_move:
        return cups
    cc_value = cups[0]
    destination = cc_value - 1
    next_three = []
    for _ in range(3):
        next_three.append(cups.pop(1))
    while destination not in cups:
        if destination > 0:
            destination -= 1
        else:
            destination = max(cups)
    destination_index = cups.index(destination)
    cups = cups[:destination_index + 1] + next_three + cups[destination_index + 1:]
    cups = cups[1:] + [cc_value]
    return play_part_1(cups, move + 1)


def print_part_1(r):
    while r[0] != 1:
        r.append(r.pop(0))
    print(''.join([str(v) for v in r[1:]]))


test_result = play_part_1(test_data[:], 1)
result = play_part_1(data[:], 1)
print_part_1(test_result)
print_part_1(result)


def play_part_2(current):
    for _ in range(10_000_000):
        picked = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]
        cups[current] = cups[picked[-1]]
        destination = (current - 1) if current > 1 else max(cups)
        while destination in picked:
            destination = (destination - 1) if destination > 1 else max(cups)
        cups[picked[-1]] = cups[destination]
        cups[destination] = picked[0]
        current = cups[current]
    print(cups[1] * cups[cups[1]])


cups = {}
data_2 = data[:] + list(range(max(data) + 1, 1_000_001))
for i in range(len(data_2)):
    if i == len(data_2) - 1:
        cups[data_2[i]] = data_2[0]
    else:
        cups[data_2[i]] = data_2[i+1]
play_part_2(data_2[0])
