f = open("data.txt", 'r')

forrest = []
for line in f:
    forrest.append(line.strip())
slope_count = 0
column = 0
row = 0
square_count = 0
tree_count = 0
product = 0

slopes = [
    {'right':1, 'down':1},
    {'right':3, 'down':1},
    {'right':5, 'down':1},
    {'right':7, 'down':1},
    {'right':1, 'down':2}
]

for slope in slopes:
    slope_count += 1
    while row < (len(forrest) - 1):
        column += slope['right']
        row += slope['down']
        if column >= len(forrest[0]):
            column -= len(forrest[0])
        if forrest[row][column] == '.':
            square_count += 1
        elif forrest[row][column] == '#':
            tree_count += 1
    print('slope', slope_count)
    print('square', square_count)
    print('tree', tree_count)
    print('----------')
    if product == 0:
        product = tree_count
    else:
        product *= tree_count
    column = 0
    row = 0
    square_count = 0
    tree_count = 0
print('product', product)
