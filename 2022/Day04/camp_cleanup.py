with open('data.txt', 'r') as file:
    section_ids_data = file.read().split('\n')

with open('test.txt', 'r') as test_file:
    section_ids_test_data = test_file.read().split('\n')

from operator import add


def create_ranges(pairs):
    # Following code is similar to:
    # splits = [''.join(list(map(str, range(*list(map(add, list(map(int, y.split('-'))), [0,1])))))) for x in section_ids for y in x.split(',')]
    # grouped = [splits[n:n+2] for n in range(0, len(splits), 2)]
    format_ranges = [list(map(int, x.split('-'))) for x in pairs]
    inclusive_range = [list(map(add, x, [0,1])) for x in format_ranges]
    generate_ranges = [list(range(*x)) for x in inclusive_range]
    # prevents issues like 4 in 323334 and others that result in dumping everything into a string
    stringify_range = [' ' + ' , '.join(list(map(str, x))) + ' ' for x in generate_ranges]
    return stringify_range


def format_data(section_ids):
    separated_pairs = [x.split(',') for x in section_ids]
    ranged_pairs = [create_ranges(x) for x in separated_pairs]
    return ranged_pairs


def find_overlap(section_ids):
    formatted_ids = format_data(section_ids)
    overlap = sum(1 for ids in formatted_ids if ids[0] in ids[1] or ids[1] in ids[0])
    return overlap


print(find_overlap(section_ids_test_data))
print(find_overlap(section_ids_data))


def create_numeric_range(pairs):
    format_ranges = [list(map(int, x.split('-'))) for x in pairs]
    inclusive_range = [list(map(add, x, [0,1])) for x in format_ranges]
    generate_ranges = [set(range(*x)) for x in inclusive_range]
    return generate_ranges


def find_partial_overlap(section_ids):
    separated_pairs = [x.split(',') for x in section_ids]
    ranged_pairs = [create_numeric_range(x) for x in separated_pairs]
    overlapped_areas = [s[0].intersection(s[1]) for s in ranged_pairs]
    overlap_count = sum(1 for x in overlapped_areas if len(x) > 0)
    return overlap_count

print(find_partial_overlap(section_ids_test_data))
print(find_partial_overlap(section_ids_data))
