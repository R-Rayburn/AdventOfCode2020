with open('test1.txt', 'r') as f: numbers = [int(x) for x in f.read().split(',') if x]

value_to_indicies = {}
step = len(numbers)
stop_step = 2020
value = numbers[step-1]
for i in range(len(numbers)):
    if numbers[i] in value_to_indicies.keys():
        value_to_indicies[numbers[i]].append(i+1)
    else:
        value_to_indicies[numbers[i]] = [i+1]

while step < stop_step:
    print(str(step) + ': ' + str(value))
    step += 1
    if len(value_to_indicies[value]) > 1:
        value = value_to_indicies[value][-1] - value_to_indicies[value][-2]
    else:
        value = 0
    if value in	value_to_indicies.keys():
        value_to_indicies[value].append(step)
    else:
        value_to_indicies[value] = [step]
    if step == stop_step:
        print(value)
