"""Historian Hysteria"""
print('Historian Hysteria')

with open('data.txt', 'r', encoding='UTF-8') as data:
    puzzle_input =  [x for x in data.read().split('\n') if x]
with open('test.txt', 'r', encoding='UTF-8') as test:
    example = [x for x in test.read().split('\n') if x]

# print(example)
# def diff_of_sorted_lists(list_1, list_2):
    # return [].append()

def organize_input(input):
    l1 = []
    l2 = []
    for a in input:
        v1, v2 = a.split()
        l1.append(int(v1))
        l2.append(int(v2))
    l1.sort()
    l2.sort()
    return l1, l2

def find_value(input):
    l1, l2 = organize_input(input)
    l2 = [x*-1 for x in l2]
    return list(map(sum, zip(l1, l2)))

print('Part 1')
print(f'Test: {sum(abs(x) for x in find_value(example))}')
print(f'Data: {sum(abs(x) for x in find_value(puzzle_input))}')

def part_2(input):
    l1, l2 = organize_input(input)
    s = 0
    for x in l1:
        s += x * l1.count(x)
    return s
# def part_2(input):
#     number_converter = {
#         'one': '1',
#         'two': '2',
#         'three': '3',
#         'four': '4',
#         'five': '5',
#         'six': '6',
#         'seven': '7',
#         'eight': '8',
#         'nine': '9',
#         'zero': '0',
#     }

#     for key in number_converter.keys():
#         input = input.replace(key, ''.join([key, number_converter[key], key]))

#     return input

    

print('Part 2')
print(f'Test: {part_2(test)}')
print(f'Data: {part_2(puzzle_input)}')