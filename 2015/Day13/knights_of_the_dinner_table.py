from itertools import permutations

print("Knights of the Dinner Table")

with open('data.txt', 'r') as file:
    seating_data = file.read().split('\n')

with open('test.txt', 'r') as test_file:
    test_seating = test_file.read().split('\n')

def format_seating_graph(seating, graph: dict):
    user, _, instance, value, *_, neighbor = seating.split(' ')
    value = int(value) if instance == 'gain' else int(value) * -1
    neighbor = neighbor.replace('.', '')
    graph.setdefault(user, {})
    # graph[user].setdefault(neighbor)
    graph[user][neighbor] = value
    return graph

def generate_graph(seating):
    graph = {}
    for s in seating:
        graph = format_seating_graph(s, graph)
    return graph


def include_me_in_graph(graph):
    keys = graph.keys()
    graph['me'] = {}
    for key in keys:
        graph['me'][key] = 0
        graph[key]['me'] = 0
    return graph


def get_seating_arrangements(seating, include_me=False):
    graph = generate_graph(seating)
    if include_me:
        graph = include_me_in_graph(graph)
    possible_orders = permutations(graph.keys())
    sums = []
    for order in possible_orders:
        sum = 0
        for i, o in enumerate(order):
            sum += graph[o][order[i-1]]
            sum += graph[order[i-1]][o]
            if i + 1 == len(order):
                sum += graph[o][order[0]]
                sum += graph[order[0]][o]
            else:
                sum += graph[o][order[i+1]]
                sum += graph[order[i+1]][o]
        sums.append(sum//2)
    return max(sums)

print('Part 1')
print(get_seating_arrangements(test_seating))
print(get_seating_arrangements(seating_data))

print('Part 2')
print(get_seating_arrangements(test_seating, True))
print(get_seating_arrangements(seating_data, True))
