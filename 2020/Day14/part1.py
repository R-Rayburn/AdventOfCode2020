with open('data.txt', 'r') as f: input_data = [x for x in f.read().split('\n') if x]

memory = {}
mask = ''

for action in input_data:
    if 'mask' in action:
        _, mask = action.split(' = ')
    else:
        address, value = action.split(' = ')
        value = int(value)
        address = address.replace('[', ' ').replace(']', '')
        _, address_value = address.split(' ')
        bin_value = bin(int(value))[2:].zfill(36)
        for i in range(len(mask)):
            if mask[i] != 'X':
                bin_value = bin_value[:i] + mask[i] + bin_value[i+1:]
        memory[address_value] = int(bin_value, 2)

s = sum([memory[key] for key in memory.keys()])
print(s)
