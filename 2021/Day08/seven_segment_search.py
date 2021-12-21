print('Seven Segment Search')

with open('data.txt', 'r') as input_data:
    entries = [d for d in input_data.read().split('\n') if d]
with open('test.txt', 'r') as test:
    test_entries = [t for t in test.read().split('\n') if t]

unique_digits = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}


def format_entry(entry):
    unique_signal_patterns, four_digit_output = entry.split(' | ')
    formatted_unique_signal_patterns = [''.join(sorted(x)) for x in unique_signal_patterns.split()]
    formatted_four_digit_output = [''.join(sorted(x)) for x in four_digit_output.split()]
    return formatted_unique_signal_patterns, formatted_four_digit_output


def get_unique_digit_output_count(entry_data):
    output = [format_entry(x)[1] for x in entry_data]
    return len([o for x in output for o in x if len(o) in unique_digits.values()])


print('Part 1')
print(f'Test: {get_unique_digit_output_count(test_entries)}')
print(f'Data: {get_unique_digit_output_count(entries)}')


def find_decoded_values(data_entries):
    decoded_values = []
    known_mappings = {2: 1, 3: 7, 4: 4, 7: 8}
    for entry in data_entries:
        mappings = {known_mappings[len(value)]: value for value in entry if len(value) in known_mappings.keys()}
        # 6
        for value in entry:
            if len(value) == 6 and any(c not in value for c in mappings[1]):
                mappings[6] = value
                break
        # 0
        for value in entry:
            if len(value) == 6 and any(c not in value for c in mappings[4]) and value != mappings[6]:
                mappings[0] = value
                break
        # 9
        for value in entry:
            if len(value) == 6 and value not in (mappings[0], mappings[6]):
                mappings[9] = value
                break
        # 5
        for value in entry:
            if len(value) == 5 and all(c in mappings[6] for c in value):
                mappings[5] = value
                break
        # 3
        for value in entry:
            if len(value) == 5 and all(c in mappings[9] for c in value) and value not in mappings.values():
                mappings[3] = value
                break
        # 2
        for value in entry:
            if len(value) == 5 and value not in mappings.values():
                mappings[2] = value
                break
        decoded_values.append({v: k for k, v in mappings.items()})
    return decoded_values


def calculate_outputs(data_entries):
    formatted_entries = [format_entry(line) for line in data_entries]
    unique_signal = [x[0] for x in formatted_entries]
    outputs = [x[1] for x in formatted_entries]
    decoded_values = find_decoded_values(unique_signal)
    total = 0
    for i, output in enumerate(outputs):
        total += int(''.join([str(decoded_values[i][o]) for o in output]))
    return total
# PROCESS:
#  - determine 1, 4, 7, 8 by length
#  - find two of three five digits
#  -- 0, 6, 9
#  -- 6 is len()=5 and has a char in 1 that is not in 6
#  -- new list is 0, 9
#  -- 0 is len()=5 and has a char in 4 that is not in 0
#  -- 9 is last value of len()=6
#  - find two of three six digits
#  -- 2, 3, 5
#  -- 5 is all digits in value are in 6 and len()=6
#  -- 3 is len()=6 and all digits in value are in 9 and not 5
#  -- 2 is last value of len()=6


print('Part 2')
print(f'Test: {calculate_outputs(test_entries)}')
print(f'Data: {calculate_outputs(entries)}')
