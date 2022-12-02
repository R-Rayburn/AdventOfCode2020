print('No Such Thing as Too Much')

with open('data.txt', 'r') as file:
    containers = [int(x) for x in file.read().split('\n')]

with open('test.txt', 'r') as test_file:
    test_containers = [int(x) for x in test_file.read().split('\n')]

from itertools import combinations

def get_combinations(c):
    combs = []
    for i in range(len(c)):
        combs.append(list(combinations(c, i)))
    return combs

def get_container_combinations_that_fit(c, size):
    container_combinations = [list(y) for x in get_combinations(c) for y in x if sum(y) == size]
    return len(container_combinations)

print('Part 1')
print(get_container_combinations_that_fit(test_containers, 25))
print(get_container_combinations_that_fit(containers, 150))

def get_count_of_min_containers_that_fit(c, size):
    container_combinations = [list(y) for x in get_combinations(c) for y in x if sum(y) == size]
    min_container_len = min([len(x) for x in container_combinations])
    min_container_count = len([x for x in container_combinations if len(x) == min_container_len])
    return min_container_count

print('Part 2')
print(get_count_of_min_containers_that_fit(test_containers, 25))
print(get_count_of_min_containers_that_fit(containers, 150))

