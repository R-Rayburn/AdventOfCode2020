"""Trebuchet"""
print('Trebuchet')

with open('data.txt', 'r', encoding='UTF-8') as data:
    puzzle_input =  [x for x in data.read().split('\n') if x]
with open('test.txt', 'r', encoding='UTF-8') as test:
    example = [x for x in test.read().split('\n') if x]
with open('test_2.txt', 'r', encoding='UTF-8') as test_2:
    example_2 = [x for x in test_2.read().split('\n') if x]

def find_value(input):
    numerics = [x for x in input if x.isnumeric()]
    return int(numerics[0] + numerics[-1])

print('Part 1')
print(f'Test: {sum([find_value(x) for x in example])}')
print(f'Data: {sum([find_value(x) for x in puzzle_input])}')


def part_2(input):
    number_converter = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0',
    }

    for key in number_converter.keys():
        input = input.replace(key, ''.join([key, number_converter[key], key]))

    return input

    

print('Part 2')
print(f'Test: {sum([find_value(part_2(x)) for x in example_2])}')
print(f'Data: {sum([find_value(part_2(x)) for x in puzzle_input])}')