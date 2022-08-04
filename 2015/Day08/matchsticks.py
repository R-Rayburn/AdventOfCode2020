import re
print('Matchsticks')

with open('data.txt', 'r') as file:
    data_strings = [x for x in file.read().split('\n') if x]

with open('test.txt', 'r') as test_file:
    test_strings = [x for x in test_file.read().split('\n') if x]


def strip_for_memory(value):
    stripped_quotes = value[1:len(value) - 1]
    removed_esc_quote = stripped_quotes.replace('\\"', 'R')
    removed_esc_slash = removed_esc_quote.replace('\\\\', 'R')
    removed_hex_char = re.sub(r'\\x(\w|\d){2}', 'R', removed_esc_slash)
    return removed_hex_char


def code_minus_memory(values):
    code = sum(len(x) for x in values)
    memory = sum(len(strip_for_memory(x)) for x in values)
    return code - memory


print('Part 1')
print(f'Test: {code_minus_memory(test_strings)}')  # 12
print(f'Data: {code_minus_memory(data_strings)}')  # 1342


def encode_string(value):
    add_esc_slash = value.replace('\\', '\\\\')
    add_esc_quote = add_esc_slash.replace('"', '\\"')
    return add_esc_quote


def encode_minus_code(values):
    code = sum(len(x) for x in values)
    encode = sum(len(encode_string(x)) + 2 for x in values)
    return encode - code


print('Part 2')
print(f'Test: {encode_minus_code(test_strings)}')
print(f'Data: {encode_minus_code(data_strings)}')
