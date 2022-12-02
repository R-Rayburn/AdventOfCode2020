print('Rock Paper Scissors')

with open('data.txt', 'r', encoding='UTF-8') as data:
    data_moves = list(data.read().split('\n'))
with open('test.txt', 'r', encoding='UTF-8') as test:
    test_moves = list(test.read().split('\n'))

# Rock     : A X
# Paper    : B Y
# Scissors : C Z

SHAPE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

OUTCOME_SCORE = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}


def calculate_score(moves):
    total = 0
    for m in moves:
        _, shape = m.split(' ')
        total += SHAPE_SCORE[shape] + OUTCOME_SCORE[m]
    return total

print('Part 1')
print(f'Test: {calculate_score(test_moves)}')
print(f'Data: {calculate_score(data_moves)}')

COMPLETE_RULES = {
    'A X': 3+0,
    'A Y': 1+3,
    'A Z': 2+6,
    'B X': 1+0,
    'B Y': 2+3,
    'B Z': 3+6,
    'C X': 2+0,
    'C Y': 3+3,
    'C Z': 1+6,
}

print('Part 2')
print(f'Test: {sum(COMPLETE_RULES[m] for m in test_moves)}')
print(f'Data: {sum(COMPLETE_RULES[m] for m in data_moves)}')