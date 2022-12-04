with open('data.txt', 'r') as file:
    rucksack_data = file.read().split('\n')

with open('test.txt', 'r') as test_file:
    test_rucksack = test_file.read().split('\n')

# a-z:1-26
# A-Z:27-52
from string import ascii_lowercase, ascii_uppercase
PRIORITY_LOOKUP = {x:ord(x)-96 for x in ascii_lowercase}
PRIORITY_LOOKUP.update({x:ord(x)-64+26 for x in ascii_uppercase})

def find_shared_value_in_rucksack_compartments(c1, c2):
    shared_value = [x for x in c1 if x in c2][0]
    return shared_value

def divide_rucksack_compartments(rucksack):
    half = len(rucksack)//2
    return rucksack[:half], rucksack[half:]

def search_rucksacks(rucksacks):
    shared_values = [find_shared_value_in_rucksack_compartments(*divide_rucksack_compartments(rucksack)) for rucksack in rucksacks]
    priority_total = sum([PRIORITY_LOOKUP[value] for value in shared_values])
    return priority_total

print(search_rucksacks(test_rucksack))
print(search_rucksacks(rucksack_data))

def find_shared_value_in_group(r1, r2, r3):
    return [x for x in r1 if x in r2 and x in r3][0]


def grouped_rucksacks_search(rucksacks):
    shared_values = [find_shared_value_in_group(*rucksacks[n:n+3]) for n in range(0, len(rucksacks), 3)]
    priority_total = sum([PRIORITY_LOOKUP[value] for value in shared_values])
    return priority_total

print(grouped_rucksacks_search(test_rucksack))
print(grouped_rucksacks_search(rucksack_data))
