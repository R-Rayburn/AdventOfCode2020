with open('data.txt', 'r') as f: numbers = [x for x in f.read().split('\n') if x]

distance = {'north': 0, 'south': 0, 'east': 0, 'west': 0}
direction = 'east'
degree = 0

def find_direction(degree, turn, degree_change):
    direction = ''
    if turn == 'R':
        degree -= degree_change
    if turn == 'L':
        degree += degree_change
    if degree <= -360:
        degree += 360
    if degree >= 360:
        degree -= 360
    if degree == 0:
        direction = 'east'
    elif degree == 90 or degree == -270:
        direction = 'north'
    elif abs(degree) == 180:
        direction = 'west'
    else:
        direction = 'south'
    return (degree, direction)
        
for i in numbers:
    command = i[0]
    value = int(i[1:])
    if command == 'R' or command == 'L':
        degree, direction = find_direction(degree, command, value)
    elif command == 'F':
        distance[direction] += value
    elif command == 'N':
        distance['north'] += value
    elif command == 'S':
        distance['south'] += value
    elif command == 'E':
        distance['east'] += value
    elif command == 'W':
        distance['west'] += value
    print(command + str(value))

print(abs(distance['east'] - distance['west']) + abs(distance['north'] - distance['south']))
