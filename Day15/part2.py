with open('data.txt', 'r') as f: numbers = [int(x) for x in f.read().split(',') if x]

valmap = {}
step = len(numbers)+1
stop_step = 30000000
value = 0
for i in range(len(numbers)):
    valmap[numbers[i]] = i+1

while step < stop_step:
    if value in valmap.keys():
        diff = step - valmap[value]
        valmap[value] = step
        value = diff
    else:
        valmap[value] = step
        value = 0
    step += 1
print(value)
