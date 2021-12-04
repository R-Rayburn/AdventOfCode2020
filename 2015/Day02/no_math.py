print('I was told there would be no math')

with open('data.txt', 'r') as file:
    dimensions_list = [x for x in file.read().split('\n') if x]


def get_sq_feet(dimensions):
    l, w, h = [int(x) for x in dimensions.split('x')]
    lw = l * w
    wh = w * h
    hl = h * l
    slack = min(lw, wh, hl)
    feet_of_wrapping = 2 * (lw+wh+hl)
    return feet_of_wrapping + slack


print('Part 1')
print(f'Test 1: {get_sq_feet("2x3x4")}')  # 58
print(f'Test 2: {get_sq_feet("1x1x10")}')  # 43
print(f'Data: {sum([get_sq_feet(x) for x in dimensions_list])}')


def get_ribbon_length(dimensions):
    l, w, h = [int(x) for x in dimensions.split('x')]
    lw = 2*l + 2*w
    wh = 2*w + 2*h
    hl = 2*h + 2*l
    smallest_side = min(lw, wh, hl)
    return smallest_side + (l*w*h)


print('Part 2')
print(f'Test 1: {get_ribbon_length("2x3x4")}')  # 34
print(f'Test 2: {get_ribbon_length("1x1x10")}')  # 14
print(f'Data: {sum([get_ribbon_length(x) for x in dimensions_list])}')
