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
        bin_value = bin(int(address_value))[2:].zfill(36)
        for i in range(len(mask)):
            if mask[i] != '0':
                bin_value = bin_value[:i] + mask[i] + bin_value[i+1:]
        floats = bin_value.count('X')
        for i in range(2**floats):
            new_address = bin_value
            new_bin = bin(i)[2:]
            new_bin = new_bin.zfill(floats)
            for j in range(len(new_bin)):
                k = new_address.find('X')
                if k > -1:
                    new_address = new_address[:k] + new_bin[j] + new_address[k+1:]
            memory[int(new_address, 2)] = value

s = sum([memory[key] for key in memory.keys()])
print(s)
