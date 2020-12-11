with open('data.txt', 'r') as f: numbers = [int(x) for x in f.read().split('\n') if x]

def find_jolts(numbers):
    numbers.sort()
    numbers.insert(0,0)
    numbers.append(3 + numbers[len(numbers)-1])
    jolt_diff = { 1: 0, 2: 0, 3: 0 }
    for i in range(1, len(numbers)):
        jolt_diff[numbers[i]-numbers[i-1]] += 1
    return jolt_diff

jolts = find_jolts(numbers)
print(jolts[1] * jolts[3])
