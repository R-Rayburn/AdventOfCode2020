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
                print(formatted_directories)
                for cd in formatted_directories:
                    files_in_directories.setdefault(cd, {})
                    files_in_directories[cd][file_name] = int(size)


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


def find_directory_to_remove(lines):
    disc_space = 70000000
    needed_unused_space = 30000000
    directories = []
    files_in_directories = {}
    read_commands(lines, directories, files_in_directories)
    directory_sizes = [sum(v.values()) for _, v in files_in_directories.items()]
    used_space = max(directory_sizes)
    unused_space = disc_space - used_space
    size_to_remove = needed_unused_space - unused_space
    removable_directories = [x for x in directory_sizes if x >= size_to_remove]
    # print(min(removable_directories) + unused_space)
    directory_to_remove = min(removable_directories)
    return directory_to_remove

print('  Part 2')
print(f'    Test: {find_directory_to_remove(test_command_list)}')
print(f'    Data: {find_directory_to_remove(command_list)}')  # 8395 is LOW
