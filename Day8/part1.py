with open('data.txt', 'r') as f: instructions = [x for x in f.read().split('\n') if x]

def get_accumulator_value():
    accumulator = 0
    index = 0
    visited_indexes = []
    while index not in visited_indexes:
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
    print(accumulator)
            

get_accumulator_value()
