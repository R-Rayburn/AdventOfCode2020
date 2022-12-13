# Way to get file paths:
# >>> a = ['/', 'a', 'cb']
# >>> ['/'.join(a[0:i+1]).replace('//', '/') for i, x in enumerate(a)]
# ['/', '/a', '/a/cb']

with open('data.txt', 'r') as file:
    command_list = file.read().split('\n')

with open('test.txt', 'r') as test_file:
    test_command_list = test_file.read().split('\n')

# CD = []
# FILES_IN_DIRECTORIES = {}


def is_command(input_string):
    return input_string[0] == '$'


def read_commands(lines: list, directories: list, files_in_directories: dict):
    for line in lines:
        if is_command(line):
            _, *command_info = line.split(' ')
            if command_info[0] == 'cd':
                if command_info[1] != '..':
                    directories.append(command_info[1])
                else:
                    directories.pop()
        else:
            size, file_name = line.split(' ')
            if size != 'dir':
                formatted_directories = ['/'.join(directories[0:i+1]).replace('//', '/') for i, _ in enumerate(directories)]
                for cd in formatted_directories:
                    files_in_directories.setdefault(cd, {})
                    print(files_in_directories[cd])
                    files_in_directories[cd][cd+file_name] = int(size)


def find_removable_file_size(lines, at_most=100000):
    directories = []
    files_in_directories = {}
    read_commands(lines, directories, files_in_directories)
    directory_sizes = [sum(files_in_directories[x].values()) for x in files_in_directories.keys()]
    removable_directories = [x for x in directory_sizes if x < at_most]
    return sum(removable_directories)

print('No space left on device')
print('  Part 1')
print(f'    Test: {find_removable_file_size(test_command_list)}')
print(f'    Data: {find_removable_file_size(command_list)}')


def execute_commands(lines: list):
    key_path = []
    directories = {}
    for line in lines:
        temp_dict = directories
        for key in key_path:
            temp_dict = temp_dict[key]
        if is_command(line):
            _, *info = line.split(' ')
            if info[0] == 'cd':
                if info[1] == '..':
                    key_path.pop()
                else:
                    key_path.append(info[1])
                    if info[1] not in temp_dict.keys():
                       temp_dict[info[1]] = {}
        else:
            size, file_name = line.split(' ')
            if size == 'dir':
                temp_dict[file_name] = {'SIZE': 0}
            else:
                if file_name not in temp_dict.keys():
                    temp_dict.setdefault('SIZE', 0)
                    temp_dict['SIZE'] += int(size)
                temp_dict[file_name] = int(size)
    return directories

TOTAL_VALUES = []

def sum_dict_values(d: dict):
    # temp_d = d
    # total = 0
    for _, value in d.items():
        if type(value) is dict:
            # d.setdefault('SIZE', 0)
            d['SIZE'] += sum_dict_values(value)
    # if total >= size_to_remove:
    # TOTAL_VALUES.append(total)
    return d['SIZE']

  
def get_sizes(d):
    for k, v in d.items():
        if isinstance(v, dict):
            yield from get_sizes(v)
        elif k == 'SIZE':
            yield v


# print(execute_commands(test_command_list))
# print(execute_commands(command_list))

def find_directory_to_remove(lines):
    disc_space = 70000000
    needed_unused_space = 30000000
    directories = []
    files_in_directories = {}
    read_commands(lines, directories, files_in_directories)
    directory_sizes = {k:sum(v.values()) for k, v in files_in_directories.items()}
    print(directory_sizes)
    used_space = max(directory_sizes.values())
    print([key for key, value in directory_sizes.items() if value == used_space])
    unused_space = disc_space - used_space
    size_to_remove = needed_unused_space - unused_space
    print(f'Size to remove is {size_to_remove}')
    removable_directories = [x for x in directory_sizes.values() if x >= size_to_remove]
    # print(min(removable_directories) + unused_space)
    directory_to_remove = min(removable_directories)
    return directory_to_remove


def find_size_v2(lines):
    disc_space = 70000000
    needed_unused_space = 30000000
    directories = execute_commands(lines)
    print(directories)
    used_space = sum_dict_values(directories['/'])
    unused_space = disc_space - used_space
    size_to_remove = needed_unused_space - unused_space
    # print(directories)
    directory_to_remove = min([x for x in get_sizes(directories['/']) if x >= size_to_remove])
    return directory_to_remove


print('  Part 2')
print(f'    Test: {find_size_v2(test_command_list)}')
print(f'    Data: {find_size_v2(command_list)}')  # 8395 is LOW
