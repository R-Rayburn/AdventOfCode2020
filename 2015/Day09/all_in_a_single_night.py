import itertools

print('All in a Single Night')

with open('data.txt', 'r') as file:
    data_edges = [x for x in file.read().split('\n') if x]

with open('test.txt', 'r') as test_file:
    test_edges = [x for x in test_file.read().split('\n') if x]


def create_node_dict(edges):
    nodes_dict = {}
    for edge in edges:
        nodes, weight = edge.split(' = ')
        n1, n2 = nodes.split(' to ')
        if n1 in nodes_dict.keys():
            nodes_dict[n1].update({n2: int(weight)})
        else:
            nodes_dict.update({n1: {n2: int(weight)}})
        if n2 in nodes_dict.keys():
            nodes_dict[n2].update({n1: int(weight)})
        else:
            nodes_dict.update({n2: {n1: int(weight)}})
    return nodes_dict


def find_distance_of_route(edges, func=min):

    nodes_dict = create_node_dict(edges)

    # return min or max
    length, ordering = func(
        # tuple containing sum of distances and path followed
        (sum(nodes_dict[src][dist]
             for src, dist in zip(ordering, ordering[1:])
             ), ordering)
        # find ordering in parallel
        for ordering in itertools.permutations(nodes_dict.keys())
    )

    return length, ordering


print('Part 1')
print(f'Test: {find_distance_of_route(test_edges)}')  # 605
print(f'Data: {find_distance_of_route(data_edges)}')  # 117

print('Part 2')
print(f'Test: {find_distance_of_route(test_edges, func=max)}')  # 982
print(f'Data: {find_distance_of_route(data_edges, func=max)}')  # 909
