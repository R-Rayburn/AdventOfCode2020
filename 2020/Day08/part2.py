with open('data.txt', 'r') as f: instructions = [x for x in f.read().split('\n') if x]

def get_accumulator_value(instructions):
    accumulator = 0
    index = 0
    visited_indexes = []
    while index not in visited_indexes and index in range(0, len(instructions)):
        instruction = instructions[index]
        operation, argument = instruction.split(' ')
        visited_indexes.append(index)
        if operation == 'nop':
            index += 1
        elif operation == 'acc':
            accumulator += int(argument)
            index += 1
        elif operation == 'jmp':
            index += int(argument)
    return accumulator

def detect_completion(instructions):
    accumulator = 0
    index = 0
    visited_indexes = []
    while index not in visited_indexes:
        if index >= len(instructions):
            return True
        instruction = instructions[index]
        operation, argument = instruction.split(' ')
        visited_indexes.append(index)
        if operation == 'nop':
            index += 1
        elif operation == 'acc':
            accumulator += int(argument)
            index += 1
        elif operation == 'jmp':
            index += int(argument)
    return False

def fix_instructions():
    for i in range(0, len(instructions)):
        if 'nop' in instructions[i]:
            instructions[i] = instructions[i].replace('nop', 'jmp')
            if detect_completion(instructions):
                print('success')
                print(get_accumulator_value(instructions))
                break
            else:
                instructions[i] = instructions[i].replace('jmp', 'nop')
        elif 'jmp' in instructions[i]:
            instructions[i] = instructions[i].replace('jmp', 'nop')
            if detect_completion(instructions):
                print('success')
                print(get_accumulator_value(instructions))
                break
            else:
                instructions[i] = instructions[i].replace('nop', 'jmp')
                
fix_instructions()
