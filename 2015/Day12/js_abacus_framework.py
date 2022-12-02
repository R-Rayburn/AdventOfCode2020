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


def total_num_sum_exclude_red(data):
    data = json.loads(data)
    print(data)
    # data = str(data)
    # return total_num_sum(data)


print('Part 1')
print(f'Data: {total_num_sum(data_json)}')
print('Part 2')
print(f'Data: {total_num_sum_exclude_red(data_json)}')