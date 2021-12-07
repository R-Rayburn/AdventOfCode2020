print('Giant Squid')

with open('data.txt', 'r') as data:
    bingo_numbers, *bingo_boards = [d for d in data.read().split('\n\n') if d]
with open('test.txt', 'r') as test:
    test_nums, *test_boards = [t for t in test.read().split('\n\n') if t]


class Cell:
    def __init__(self, value):
        self.value = int(value)
        self.marked = False

    def mark_cell(self):
        self.marked = True

    def __repr__(self):
        return f'Value: {self.value}' + (' is marked' if self.marked else ' is not marked')


class Board:
    def __init__(self, rows):
        self.rows = rows
        self.values = {c.value: False for r in rows for c in r}

    def add_row(self, row):
        self.rows.append(row)

    def mark_cell(self, value):
        for row in self.rows:
            for cell in row:
                if cell.value == value:
                    cell.mark_cell()
                    self.values[cell.value] = True

    def get_winning_row(self):
        for row in self.rows:
            if all([cell.marked for cell in row]):
                return row
        return []  # if a winning row is on the board

    def get_winning_column(self):
        for i in range(len(self.rows[0])):
            column = [r[i] for r in self.rows]
            if all([c.marked for c in column]):
                return column
        return []

    def get_unmarked_values(self):
        return [k for k in self.values.keys() if self.values[k] is False]

    def __repr__(self):
        return f'Board: {self.rows}'


def format_numbers(nums):
    return [int(n) for n in nums.split(',')]


def format_boards(boards):
    # formatted_boards = []
    # for board in boards:
    #     new_board = Board([])
    #     for row in board.split('\n'):
    #         new_board.add_row([Cell(cell) for cell in row.split()])
    #     formatted_boards.append(new_board)
    # return formatted_boards
    return [Board([[Cell(cell) for cell in row.split()] for row in board.split('\n')]) for board in boards]


def find_winning_numbers(numbers, boards):
    number_list = format_numbers(numbers)
    formatted_boards = format_boards(boards)
    for number in number_list:
        for board in formatted_boards:
            board.mark_cell(number)
            winning_row = board.get_winning_row()
            winning_col = board.get_winning_column()
            if len(winning_row) > 0 or len(winning_col) > 0:
                return board, number
    return None, None


def calculate_score(numbers, boards):
    # score is sum of unmarked numbers on winning board and multiply that by number that was found
    winning_board, last_number = find_winning_numbers(numbers, boards)
    sum_of_unmarked = sum(winning_board.get_unmarked_values())
    return sum_of_unmarked * last_number


print('Part 1')
print(f'Test: {calculate_score(test_nums, test_boards)}')
print(f'Data: {calculate_score(bingo_numbers, bingo_boards)}')


def find_losing_board(numbers, boards):
    number_list = format_numbers(numbers)
    formatted_boards = format_boards(boards)
    winning_boards = []
    for number in number_list:
        for board in [b for b in formatted_boards if b not in winning_boards]:
            board.mark_cell(number)
            winning_row = board.get_winning_row()
            winning_col = board.get_winning_column()
            if len(winning_row) > 0 or len(winning_col) > 0:
                if len(formatted_boards) != 1:
                    formatted_boards.remove(board)
                else:
                    return board, number
                # winning_boards.append(board)
                # remove board
        # for board in winning_boards:
        #     formatted_boards.remove(board)
        # winning_boards = []
        # if len(formatted_boards) == 1:
        #     return formatted_boards[0], number
    return None, None
    # go through boards
    # for each number
    #   for each board
    #       mark cell
    #       if winning board
    #           remove board
    #   if boards == 1
    #       return board, number


def calc_losing_board_score(numbers, boards):
    last_winning_board, last_number = find_losing_board(numbers, boards)
    sum_of_unmarked = sum(last_winning_board.get_unmarked_values())
    return sum_of_unmarked * last_number


print('Part 2')
print(f'Test: {calc_losing_board_score(test_nums, test_boards)}')
print(f'Data: {calc_losing_board_score(bingo_numbers, bingo_boards)}')
