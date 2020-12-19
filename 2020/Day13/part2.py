with open('data.txt', 'r') as f: input_data = [x for x in f.read().split('\n') if x]

bus_times = [x for x in input_data[1].split(',') if x]
bus_index = {}

for x in range(len(bus_times)):
    if bus_times[x] != 'x':
        bus_index[int(bus_times[x])] = x

def divisible_value_not_evenly_divisible(value, index, bus):
    return (value + index) % bus != 0
        
divisible_value=0
combined_product = 1
for bus in bus_index.keys():
    # find new bus+index value that is divisible by new bus including previous buses
    while divisible_value_not_evenly_divisible(divisible_value, bus_index[bus], bus):
        # increase the divisible value by the divisible product of the previous values
        divisible_value += combined_product
    # increase divisible product by including new bus
    combined_product *= bus

print(divisible_value)
