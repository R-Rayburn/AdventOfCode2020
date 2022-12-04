with open('data.txt', 'r') as file:
    section_ids_data = file.read().split('\n')

with open('test.txt', 'r') as test_file:
    section_ids_test_data = test_file.read().split('\n')

from operator import add

def format_data(section_ids):
    # splits = [x.split(',') for x in section_ids]
    # splits = [''.join(list(map(str, range(*list(map(int, y.split('-'))))))) for x in section_ids for y in x.split(',')]
    # splits = [list(map(add, list(map(int, y.split('-'))), [0,1])) for x in section_ids for y in x.split(',')]
    splits = [''.join(list(map(str, range(*list(map(add, list(map(int, y.split('-'))), [0,1])))))) for x in section_ids for y in x.split(',')]
    grouped = [splits[n:n+2] for n in range(0, len(splits), 2)]
    return grouped

def find_overlap(section_ids):
    formatted_ids = format_data(section_ids)
    overlap = 0
    for ids in formatted_ids:
        if ids[0] in ids[1] or ids[1] in ids[0]:
            overlap += 1
    return overlap

print(find_overlap(section_ids_test_data))
print(find_overlap(section_ids_data)). # 588 is WRONG