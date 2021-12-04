print('Sonar Sweep')

with open('data.txt', 'r') as data:
    data_numbers = [int(x) for x in data.read().split('\n') if x]
with open('test.txt', 'r') as test:
    test_numbers = [int(x) for x in test.read().split('\n') if x]


def find_increases(file_info):
    increase_count = 0
    for i in range(1, len(file_info)):
        if file_info[i-1] < file_info[i]:
            increase_count += 1
    return increase_count


print('Part 1')
print(f'Test Answer: {find_increases(test_numbers)}')
print(f'Data Answer: {find_increases(data_numbers)}')


def find_increases_in_three(file_info):
    increase_count = 0
    for i in range(1, len(file_info)-2):
        if file_info[i-1] + file_info[i] + file_info[i+1] < file_info[i] + file_info[i+1] + file_info[i+2]:
            increase_count += 1
    return increase_count


print('Part 2')
print(f'Test Answer: {find_increases_in_three(test_numbers)}')
print(f'Data Answer: {find_increases_in_three(data_numbers)}')
