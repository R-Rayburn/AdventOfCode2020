print('Syntax Scoring')

with open('data.txt', 'r') as input_data:
    syntax_info = [d for d in input_data.read().split('\n') if d]
with open('test.txt', 'r') as test:
    test_syntax_info = [t for t in test.read().split('\n') if t]

open_values = ['(', '[', '{', '<']
score_values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
syntax_values = ['()', '[]', '{}', '<>']


def filter_out_correct_syntax(line):
    while len([v for v in syntax_values if v in line]) > 0:
        for v in syntax_values:
            line = line.replace(v, '')
    return line


def find_score_for_line(line):
    for li in line:
        if li not in open_values:
            return score_values[li]
    return 0


def find_total_index_error_score(info):
    score = 0
    for line in info:
        reduced_line = filter_out_correct_syntax(line)
        score += find_score_for_line(reduced_line)
    return score


print('Part 1')
print(f'Test: {find_total_index_error_score(test_syntax_info)}')
print(f'Data: {find_total_index_error_score(syntax_info)}')

addition_score_values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
complementing_value = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}


def find_completion_line_score(line):
    score = 0
    for x in line:
        score = score * 5 + addition_score_values[x]
    return score


def find_completion_score(info):
    completion_scores = []
    for line in info:
        reduced_line = filter_out_correct_syntax(line)
        if find_score_for_line(reduced_line) == 0:
            completion_line = ''
            for x in reversed(reduced_line):
                completion_line += complementing_value[x]
            completion_scores.append(find_completion_line_score(completion_line))

    return sorted(completion_scores)[len(completion_scores)//2]


print('Part 2')
print(f'Test: {find_completion_score(test_syntax_info)}')
print(f'Data: {find_completion_score(syntax_info)}')
