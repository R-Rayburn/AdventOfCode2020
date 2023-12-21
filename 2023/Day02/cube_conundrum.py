"""Cube Conundrum"""
print('Cube Conundrum')

def color_converter(game):
    # (r,g,b)
    sets = game.split(': ')[-1]
    colors = [counts.split(', ') for counts in sets.split('; ')]
    return_sets = []
    for color_set in colors:
        red = 0
        blue = 0
        green = 0
        for value in color_set:
            if 'red' in value:
                red = int(value.split(' ')[0])
            elif 'blue' in value:
                blue = int(value.split(' ')[0])
            elif 'green' in value:
                green = int(value.split(' ')[0])
        return_sets.append((red, blue, green))
    return return_sets



with open('puzzle.txt', 'r', encoding='UTF-8') as data:
    puzzle_input =  [color_converter(x) for x in data.read().split('\n') if x]
with open('example.txt', 'r', encoding='UTF-8') as example:
    example_input = [color_converter(x) for x in example.read().split('\n') if x]


def find_value(index, input):
    #r = 12
    rs = [r for r, _, _ in input if r > 12]
    #b = 14
    bs = [b for _, b, _ in input if b > 14]
    #g = 13
    gs = [g for _, _, g in input if g > 13]
    
    return index+1 if len(rs) == 0 and len(bs) == 0 and len(gs) == 0 else 0

print('Part 1')
print(f'Test: {sum([find_value(i, x) for i, x in enumerate(example_input)])}')
print(f'Data: {sum([find_value(i, x) for i, x in enumerate(puzzle_input)])}')

def part_2(input):
    r = max([r for r, _, _ in input]) or 1
    b = max([b for _, b, _ in input]) or 1
    g = max([g for _, _, g in input]) or 1
    return r*b*g
    

print('Part 2')
print(f'Test: {sum([part_2(x) for x in example_input])}')
print(f'Data: {sum([part_2(x) for x in puzzle_input])}')