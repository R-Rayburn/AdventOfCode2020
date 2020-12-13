with open('data.txt', 'r') as f: input_data = [x for x in f.read().split('\n') if x]

time = int(input_data[0])
bus_times = [int(x) for x in input_data[1].split(',') if x and x != 'x']
times_after_arrival = {}


for t in bus_times:
    time_after = t
    while time_after < time:
        time_after += t
    times_after_arrival[t] = time_after

lowest_diff = float('inf')
best_bus = 0
for t in bus_times:
    if times_after_arrival[t] - time < lowest_diff:
        lowest_diff = times_after_arrival[t] - time
        best_bus = t

print(lowest_diff * best_bus)
