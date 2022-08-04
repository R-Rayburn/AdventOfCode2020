print('Some Assembly Required')

with open('data.txt', 'r') as file:
    operations = [x for x in file.read().split('\n') if x]

with open('test.txt', 'r') as test_file:
    test_operations = [x for x in test_file.read().split('\n') if x]


class BitOp:
    def __init__(self, operation=None, value1=None, value2=None, result=None):
        self.operation = operation
        self.value1 = value1
        self.value2 = value2
        self.result = result

    def __repr__(self):
        return f'[ operation: {self.operation} | value1: {self.value1} | value2: {self.value2} | result: {self.result} ]'


def dict_ops(ops):
    mapped_ops = {}
    for op in ops:
        operation, key = op.split(' -> ')
        if len(operation.split()) == 1:
            mapped_ops[key] = BitOp(result=operation)
        elif operation.isnumeric():
            mapped_ops[key] = BitOp(result=operation)
        else:
            if 'NOT' in operation:
                o, v1 = operation.split()
                mapped_ops[key] = BitOp(operation=o, value1=v1)
            else:
                v1, o, v2 = operation.split()
                mapped_ops[key] = BitOp(operation=o, value1=v1, value2=v2)
    return mapped_ops


def perform_not_operation(value):
    return 65535 - int(value)


def perform_operation(operation, value1, value2):
    if operation == 'LSHIFT':
        return int(value1) << int(value2)
    elif operation == 'RSHIFT':
        return int(value1) >> int(value2)
    elif operation == 'OR':
        return int(value1) | int(value2)
    else:
        return int(value1) & int(value2)


# TODO: solve for number being on left side of op
def solve_signal(mo, op):
    if type(op) == int:
        return op
    elif op.result is not None and not str(op.result).isnumeric():
        op.result = solve_signal(mo, mo[op.result])
    elif op.result is not None:
        return op.result
    elif op.operation == 'NOT':
        op.result = perform_not_operation(solve_signal(mo, mo[op.value1]))
    elif op.operation == 'LSHIFT' or op.operation == 'RSHIFT':
        op.result = perform_operation(op.operation, solve_signal(mo, mo[op.value1]), op.value2)
    else:
        if op.value1.isnumeric():
            op.result = perform_operation(op.operation, op.value1, solve_signal(mo, mo[op.value2]))
        elif op.value2.isnumeric():
            op.result = perform_operation(op.operation, solve_signal(mo, mo[op.value1]), op.value2)
        else:
            op.result = perform_operation(op.operation, solve_signal(mo, mo[op.value1]), solve_signal(mo, mo[op.value2]))
    return op.result


def connect_signal(input_operations, value, part=1):
    mapped_ops = dict_ops(input_operations)
    if part == 2:
        mapped_ops['b'].result = 956
    result = solve_signal(mapped_ops, mapped_ops[value])
    return result


print('Part 1')
print(f'Test d: {connect_signal(test_operations, "d")}')  # 123
print(f'Test e: {connect_signal(test_operations, "e")}')  # 123
print(f'Test f: {connect_signal(test_operations, "f")}')  # 123
print(f'Test g: {connect_signal(test_operations, "g")}')  # 123
print(f'Test h: {connect_signal(test_operations, "h")}')  # 123
print(f'Test i: {connect_signal(test_operations, "i")}')  # 123
print(f'Data: {connect_signal(operations, "a")}')

print('Part 2')
print(f'Data: {connect_signal(operations, "a", 2)}')
