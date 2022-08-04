print('Doesn\'t He Have Intern-Elves For This?')

with open('data.txt', 'r') as file:
    strings = [x for x in file.read().split('\n') if x]

with open('test.txt', 'r') as test_file:
    test_strings = [x for x in test_file.read().split('\n') if x]

with open('test2.txt', 'r') as test2_file:
    test2_strings = [x for x in test2_file.read().split('\n') if x]


def has_bad_substrings(data):
    bad_sub_strings = ['ab', 'cd', 'pq', 'xy']
    for x in bad_sub_strings:
        if x in data:
            return True
    return False


def has_enough_vowels(data):
    vowels = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    for d in data:
        if d in vowels.keys():
            vowels[d] += 1
    return sum([vowels[k] for k in vowels if vowels[k] > 0]) > 2


def has_repeating_characters(data):
    for i in range(len(data) - 1):
        if data[i] == data[i+1]:
            return True
    return False


def count_nice_strings(string_data):
    nice_strings = 0
    for d in string_data:
        if (not has_bad_substrings(d)) and has_enough_vowels(d) and has_repeating_characters(d):
            nice_strings += 1
    return nice_strings


print('Part 1')
print(f'Test: {count_nice_strings(test_strings)}')  # 2
print(f'Data: {count_nice_strings(strings)}')


def contains_non_overlapping_pattern_of_2(data):
    import re
    for i in range(len(data) - 2):
        indices_obj = re.finditer(pattern=data[i:i+2], string=data)
        indices = [index.start() for index in indices_obj]
        values = [indices[j+1] - indices[j] for j in range(len(indices) - 1)]
        values = [x for x in values if x != 1]
        if len(values) == 0:
            continue
        else:
            return True
    return False


def contains_one_repeating_character_with_single_character_between(data):
    for i in range(len(data) - 2):
        if data[i] == data[i+2]:
            return True
    return False


def count_improved_nice_strings(data):
    nice_strings = 0
    for d in data:
        if contains_non_overlapping_pattern_of_2(d) and contains_one_repeating_character_with_single_character_between(d):
            nice_strings += 1
    return nice_strings


print('Part 2')
print(f'Test: {count_improved_nice_strings(test2_strings)}')
print(f'Data: {count_improved_nice_strings(strings)}')
