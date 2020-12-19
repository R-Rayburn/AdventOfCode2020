with open('data.txt', 'r') as f: numbers = [x for x in f.read().split('\n') if x]

def find_direction(degree, turn, degree_change):
    direction1 = ''
    direction2 = ''
    if turn == 'R':
        degree -= degree_change
    if turn == 'L':
        degree += degree_change
    if degree <= -360:
        degree += 360
    if degree >= 360:
        degree -= 360
    if degree == 0:
        direction1 = 'east'
        direction2 = 'north'
    elif degree == 90 or degree == -270:
        direction1 = 'north'
        direction2 = 'west'
    elif abs(degree) == 180:
        direction1 = 'west'
        direction2 = 'south'
    else:
        direction1 = 'south'
        direction2 = 'east'
    return (degree, direction1, direction2)


distance = {'north': 0, 'south': 0, 'east': 0, 'west': 0}
 
degree = 0
waypoint_direction1 = 'east'
waypoint_direction2 = 'north'
waypoint_magnitude1 = 10
waypoint_magnitude2 = 1

for i in numbers:
    command = i[0]
    value = int(i[1:])
    if command == 'R' or command == 'L':
        degree, waypoint_direction1, waypoint_direction2 = find_direction(degree, command, value)
    elif command == 'F':
        distance[waypoint_direction1] += value * waypoint_magnitude1
        distance[waypoint_direction2] += value * waypoint_magnitude2
    elif command == 'N':
        if waypoint_direction1 == 'north':
            waypoint_magnitude1 += value
        elif waypoint_direction1 == 'south':
            waypoint_magnitude1 -= value
        elif waypoint_direction2 == 'north':
            waypoint_magnitude2 += value
        elif waypoint_direction2 == 'south':
            waypoint_magnitude2 -= value
    elif command == 'S':
        if waypoint_direction1 == 'south':
            waypoint_magnitude1 += value
        elif waypoint_direction1 == 'north':
            waypoint_magnitude1 -= value
        elif waypoint_direction2 == 'south':
            waypoint_magnitude2 += value
        elif waypoint_direction2 == 'north':
            waypoint_magnitude2 -= value
    elif command == 'E':
        if waypoint_direction1 == 'east':
            waypoint_magnitude1 += value
        elif waypoint_direction1 == 'west':
            waypoint_magnitude1 -= value
        elif waypoint_direction2 == 'east':
            waypoint_magnitude2 += value
        elif waypoint_direction2 == 'west':
            waypoint_magnitude2 -= value
    elif command == 'W':
        if waypoint_direction1 == 'west':
            waypoint_magnitude1 += value
        elif waypoint_direction1 == 'east':
            waypoint_magnitude1 -= value
        elif waypoint_direction2 == 'west':
            waypoint_magnitude2 += value
        elif waypoint_direction2 == 'east':
            waypoint_magnitude2 -= value

print(abs(distance['east'] - distance['west']) + abs(distance['north'] - distance['south']))
