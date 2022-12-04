with open('data.txt', 'r') as file:
    section_ids_data = file.read().split('\n')

with open('test.txt', 'r') as test_file:
    section_ids_test_data = test_file.read().split('\n')

from operator import add

def format_data(section_ids):
    # splits = [x.split(',') for x in section_ids]
    # splits = [''.join(list(map(str, range(*list(map(int, y.split('-'))))))) for x in section_ids for y in x.split(',')]
    splits = [list(map(int, y.split('-'))) for x in section_ids for y in x.split(',')]
    # Need to add 1 to right value to make inclusive range.
    # The following doesn't work because it is a list of lists
    inclusive_lists = [[0,1] for _ in range(len(splits))]
    inclusive = [list(map(add, splits,inclusive_lists))]
    id_ranges = 