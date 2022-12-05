with open('data.txt', 'r') as file:
    crate_data, move_instructions = file.read().split('\n\n')

with open('test.txt', 'r') as test_file:
    crate_test_data, move_test_instructions = test_file.read().split('\n\n')


def format_crate_data(crates):
    formatted_crates = [x for x in crates.split('\n')]
    number_list = formatted_crates.pop()
    indecies_to_split = [i for i in range(len(number_list)) if number_list.startswith('   ', i)]
    f_crate_2 = []
    for crate in formatted_crates:
        c = crate
        for i in indecies_to_split:
            c = c[:i] + ',' + c[i+1:]
        f_crate_2.append(c)
    
    formatted_crates = [x.split(',') for x in f_crate_2]
    crate_dict = {}
    for crate in formatted_crates:
        for i, value in enumerate(crate):
            crate_dict.setdefault(i, [])
            crate_dict[i].append(value)
    formatted_crates = [[y.replace(']', '') for y in x if y.replace(']', '')] for x in crate_dict.values()]
    formatted_crates = [[y.replace('[', '').replace(' ', '') for y in x] for x in formatted_crates]
    formatted_crates = [[y for y in x if y] for x in formatted_crates]
    for crate in formatted_crates:
        crate.reverse()
    return formatted_crates


def format_instruction(instruction):
    _, count, _, stack_1, _, stack_2 = instruction.split(' ')
    return int(count), int(stack_1), int(stack_2)


def move_crates(crates, instructions):
    crate_layout = format_crate_data(crates)
    for instruction in instructions.split('\n'):
        count, stack_1, stack_2 = format_instruction(instruction)
        for _ in range(count):
            crate_layout[stack_2-1].append(crate_layout[stack_1-1].pop())
    return crate_layout


def get_top_crates(crates, instructions):
    final_layout = move_crates(crates, instructions)
    top_crates = ''.join(x.pop() for x in final_layout)
    return top_crates


print(get_top_crates(crate_test_data, move_test_instructions))
print(get_top_crates(crate_data, move_instructions))

def move_crates_9001(crates, instructions):
    crate_layout = format_crate_data(crates)
    for instruction in instructions.split('\n'):
        count, stack_1, stack_2 = format_instruction(instruction)
        crates_to_move = [crate_layout[stack_1-1].pop() for _ in range(count)]
        crates_to_move.reverse()
        crate_layout[stack_2-1].extend(crates_to_move)
    return crate_layout

def get_new_top_crates(crates, instructions):
    final_layout = move_crates_9001(crates, instructions)
    top_crates = ''.join(x.pop() for x in final_layout)
    return top_crates


print(get_new_top_crates(crate_test_data, move_test_instructions))
print(get_new_top_crates(crate_data, move_instructions))
