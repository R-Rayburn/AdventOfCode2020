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

        if len(top_board) < len(bottom_board):
            top_board = [['.' for _ in range(len(top_board[0]))]
                         for _ in range(len(bottom_board)-len(top_board))] + top_board
        elif len(top_board) > len(bottom_board):
            bottom_board = bottom_board + [['.' for _ in range(len(top_board[0]))]
                                           for _ in range(len(top_board)-len(bottom_board))]

        for i in range(len(top_board)):
            row = top_board[i]
            for j in range(len(top_board[i])):
                if bottom_board[-i-1][j] == '#':
                    row[j] = '#'
            new_board.append(row)
    elif direction == 'x':
        left_board = [row[:line] for row in board]
        right_board = [row[line+1:] for row in board]
        if len(left_board[0]) < len(right_board[0]):
            for i in range(len(left_board)):
                left_board[i] = ['.' for _ in range(len(right_board[i]-len(left_board[i])))] + left_board[i]
        elif len(left_board[0]) > len(right_board[0]):
            for i in range(len(right_board)):
                right_board[i] = right_board[i] + ['.' for _ in range(len(left_board[i])-len(right_board[i]))]
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
    board = fold_board(board, instructions[0])
    visible_dot_count = count_visible_dots(board)
    return visible_dot_count


print('Part 1')
print(f'Test: {fold_one(test_puzzle_input)}')
print(f'Data: {fold_one(puzzle_input)}')


def fold_all(puzzle):
    coordinates, instructions = get_coordinates_and_instructions(puzzle)
    board = pin_coordinates(coordinates)
    for instruction in instructions:
        board = fold_board(board, instruction)
    print_board(board)
    return count_visible_dots(board)


print('Part 2')
print(f'Test: {fold_all(test_puzzle_input)}')
print(f'Data: {fold_all(puzzle_input)}')
