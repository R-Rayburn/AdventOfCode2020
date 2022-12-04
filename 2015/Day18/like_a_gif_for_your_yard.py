with open('data.txt', 'r') as file:
    containers = file.read().split('\n')

with open('test.txt', 'r') as test_file:
    test_containers = test_file.read().split('\n')

def switch_lights(current_state, new_state):
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if current_state[i][j] == '.':
                pass