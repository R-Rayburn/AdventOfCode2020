print('Extended Polymerization')

with open('data.txt', 'r') as data_file:
    input_data = [d for d in data_file.read().split('\n\n') if d]
with open('test.txt', 'r') as test_file:
    test_data = [t for t in test_file.read().split('\n\n') if t]


def get_template_and_rules(data):
    template = data[0]
    rules = {}
    for rule in data[1].split('\n'):
        key, value = rule.split(' -> ')
        rules[key] = value
    return template, rules


def get_polymer_template(template, rules):
    template_to_add = ''
    new_template = ''
    for i in range(len(template) - 1):
        template_to_add += rules[template[i] + template[i + 1]]
    for i in range(len(template_to_add)):
        new_template += template[i] + template_to_add[i]
    return new_template + template[-1]


def get_counts(template):
    counts = {}
    for t in template:
        if t in counts.keys():
            counts[t] += 1
        else:
            counts[t] = 1
    return counts.values()


def solve_quantity_diff(data, steps):
    template, rules = get_template_and_rules(data)
    for _ in range(steps):
        template = get_polymer_template(template, rules)
    counts = get_counts(template)
    return max(counts) - min(counts)


print('Part 1')
print(f'Test: {solve_quantity_diff(test_data, 10)}')
print(f'Data: {solve_quantity_diff(input_data, 10)}')


# def find_middle_value(key, rules, current_depth, max_depth):
#     value = rules[key]
#     if current_depth == max_depth:
#         return value
#     return find_middle_value(key[0]+value,
#                              rules,
#                              current_depth + 1,
#                              max_depth) + value + find_middle_value(value+key[1],
#                                                                     rules,
#                                                                     current_depth + 1,
#                                                                     max_depth)

from collections import defaultdict


def create_counter(values):
    return {k: 0 for k in set(values)}


def count_occurrences(counts, key, rules, current_depth, max_depth):
    if current_depth == max_depth:
        return
    value = rules[key]
    counts[value] += 1
    count_occurrences(counts, key[0]+value, rules, current_depth+1, max_depth)
    count_occurrences(counts, value+key[1], rules, current_depth+1, max_depth)


def solve_quantity_diff(data, steps):
    # Doesn't solve
    template, rules = get_template_and_rules(data)
    templates = [template[i]+template[i+1] for i in range(len(template)-1)]
    single_counts = create_counter(rules.values())
    pair_counts = create_counter(rules.keys())
    for t in template:
        single_counts[t] += 1
    for t in templates:
        pair_counts[t] += 1
    for _ in range(steps):
        new_pair_counts = defaultdict(int)
        for pair, current_count in pair_counts.items():
            added_value = rules[pair]
            new_pairs = [pair[0] + added_value, added_value + pair[1]]
            for np in new_pairs:
                new_pair_counts[np] += current_count
            single_counts[added_value] += 1
        pair_counts = new_pair_counts
    # for t in templates:
    #     counts[t] += 1
    # for t in templates:
    #     count_occurrences(counts, t, rules, 0, steps)
    return max(single_counts.values()) - min(single_counts.values())


print('Part 2')
print(f'Test: {solve_quantity_diff(test_data, 10)}')
# print(f'Data: {fold_all(puzzle_input)}')
