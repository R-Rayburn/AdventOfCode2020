print('Probably a Fire Hazard')

with open('data.txt', 'r') as file:
    santa_commands = [x for x in file.read().split('\n') if x]

with open('test.txt', 'r') as test_file:
    test_commands = [x for x in test_file.read().split('\n') if x]


def turn_command(grid, turn, start_p, end_p):
    if turn == 'on':
        for i in range(int(start_p[0]), int(end_p[0]) + 1):
            for j in range(int(start_p[1]), int(end_p[1]) + 1):
                grid[i][j] = 1
    else:
        for i in range(int(start_p[0]), int(end_p[0]) + 1):
            for j in range(int(start_p[1]), int(end_p[1]) + 1):
                grid[i][j] = -1


def toggle_command(grid, start_p, end_p):
    for i in range(int(start_p[0]), int(end_p[0]) + 1):
        for j in range(int(start_p[1]), int(end_p[1]) + 1):
            grid[i][j] *= -1


def perform_commands(commands):
    grid = [[-1 for _ in range(1000)] for _ in range(1000)]
    for command in commands:
        if command.find('turn') != -1:
            formatted_command = command.split()
            turn = formatted_command[1]
            start_point = formatted_command[2].split(',')
            end_point = formatted_command[4].split(',')
            turn_command(grid, turn, start_point, end_point)
        else:
            formatted_command = command.split()
            start_point = formatted_command[1].split(',')
            end_point = formatted_command[3].split(',')
            toggle_command(grid, start_point, end_point)
    return sum(x for y in grid for x in y if x == 1)


print('Part 1')
print(f'Test: {perform_commands(test_commands)}')  # 2
print(f'Data: {perform_commands(santa_commands)}')


def adjust_command(grid, turn, start_p, end_p):
    if turn == 'on':
        for i in range(int(start_p[0]), int(end_p[0]) + 1):
            for j in range(int(start_p[1]), int(end_p[1]) + 1):
                grid[i][j] += 1
    else:
        for i in range(int(start_p[0]), int(end_p[0]) + 1):
            for j in range(int(start_p[1]), int(end_p[1]) + 1):
                grid[i][j] -= 1
                if grid[i][j] < 0:
                    grid[i][j] = 0


def increase_command(grid, start_p, end_p):
    for i in range(int(start_p[0]), int(end_p[0]) + 1):
        for j in range(int(start_p[1]), int(end_p[1]) + 1):
            grid[i][j] += 2


def perform_actual_commands(commands):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for command in commands:
        if command.find('turn') != -1:
            formatted_command = command.split()
            turn = formatted_command[1]
            start_point = formatted_command[2].split(',')
            end_point = formatted_command[4].split(',')
            adjust_command(grid, turn, start_point, end_point)
        else:
            formatted_command = command.split()
            start_point = formatted_command[1].split(',')
            end_point = formatted_command[3].split(',')
            increase_command(grid, start_point, end_point)
    return sum(x for y in grid for x in y)


print('Part 2')
print(f'Test: {perform_actual_commands(test_commands)}')
print(f'Data: {perform_actual_commands(santa_commands)}')  # 14747699 too low
