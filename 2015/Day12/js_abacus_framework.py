print('JSAbacusFramework.io')

import string
import json

with open('data.txt', 'r') as file:
    data_json = file.read()

with open('test.txt', 'r') as test_file:
    test_json = test_file.read()


def total_num_sum(data):
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.replace('{', '')
    data = data.replace('}', '')
    data = data.replace('"', '')
    data = data.replace(':', '')
    data = ''.join([x for x in data if x not in string.ascii_lowercase])
    data = [int(x) for x in data.split(',') if x]
    return sum(data)



print('Part 1')
print(f'Data: {total_num_sum(data_json)}')


def total_num_sum_exclude_red(data, total_value):
    if isinstance(data, int):
        return data + total_value
    if isinstance(data, dict) and 'red' not in data.values():
        for value in data.values():
            total_value = total_num_sum_exclude_red(value, total_value)
    elif isinstance(data, list):
        for value in data:
            total_value = total_num_sum_exclude_red(value, total_value)
    return total_value


print('Part 2')
print(f'Data: {total_num_sum_exclude_red(json.loads(data_json), 0)}')