import itertools

print('Elves Look, Elves Say')


def play_game(sequence, steps):
    for i in range(steps):
        split_input = [''.join(g) for _, g in itertools.groupby(sequence)]
        new_seq = ''
        for new_input in split_input:
            new_seq += str(len(new_input)) + new_input[0]
        sequence = new_seq
    return len(sequence)


print('Part 1')
print(f'Test: {play_game("1", 5)}')
print(f'Data: {play_game("1113122113", 40)}')

print('Part 2')
print(f'Data: {play_game("1113122113", 50)}')
