f = open("data.txt", 'r')

forrest = []
for line in f:
    forrest.append(line.strip())
column = 0
row = 0
square_count = 0
tree_count = 0

while row < (len(forrest) - 1):
    column += 3
    row += 1
    if column >= len(forrest[0]):
        column -= len(forrest[0])
    if forrest[row][column] == '.':
        square_count += 1
    elif forrest[row][column] == '#':
        tree_count += 1
print('square', square_count)
print('tree', tree_count)
