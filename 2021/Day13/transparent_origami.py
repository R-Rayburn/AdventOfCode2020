print('Transparent Origami')

with open('data.txt', 'r') as input_data:
    puzzle_input = [d for d in input_data.read().split('\n\n') if d]
with open('test.txt', 'r') as test:
    test_puzzle_input = [t for t in test.read().split('\n\n') if t]


def get_coordinates_and_instructions(puzzle):
    coordinates = [tuple([int(x)
                          for x in p.split(',')])
                   for p in puzzle[0].split('\n')]
    instructions = [tuple([int(y) if y.isnumeric() else y
                           for y in tuple(x.split())[2].split('=')])
                    for x in puzzle[1].split('\n')]
    return coordinates, instructions


def create_board(coordinates):
    max_x = max([c[0] for c in coordinates])
    max_y = max([c[1] for c in coordinates])
    row = ['.' for _ in range(max_x + 1)]
    col = [row.copy() for _ in range(max_y + 1)]
    return col


def pin_coordinates(coordinates):
    board = create_board(coordinates)
    for x, y in coordinates:
        board[y][x] = '#'
    return board


def print_board(board):
    for row in board:
        print(''.join(row))


def fold_board(board, instructions):
    direction = instructions[0]
    line = instructions[1]
    new_board = []
    if direction == 'y':
        top_board = board[:line]
        bottom_board = board[line+1:]
        for i in range(len(top_board)):
            row = top_board[i]
            for j in range(len(top_board[i])):
                if bottom_board[-i-1][j] == '#':
                    row[j] = '#'
            new_board.append(row)
    # Need to add logic for even size boards
    elif direction == 'x':
        left_board = [row[:line] for row in board]
        right_board = [row[line+1:] if len(row)%2==0 else row[line:] for row in board]
        for i in range(len(left_board)):
            row = left_board[i]
            for j in range(len(left_board[i])):
                if right_board[i][-j-1] == '#':
                    row[j] = '#'
            new_board.append(row)
    return new_board


def count_visible_dots(board):
    return len([y for x in board for y in x if y == '#'])


def fold_one(puzzle):
    coordinates, instructions = get_coordinates_and_instructions(puzzle)
    board = pin_coordinates(coordinates)
    print(len(board[0]))
    board = fold_board(board, instructions[0])
    visible_dot_count = count_visible_dots(board)
    return visible_dot_count


print('Part 1')
print(f'Test: {fold_one(test_puzzle_input)}')
print(f'Data: {fold_one(puzzle_input)}')


# print('Part 2')
# print(f'Test: {get_path_count_p2(test_one_cave_map)}')
# print(f'Data: {get_path_count_p2(cave_map)}')
