with open('data.txt', 'r') as f: numbers = [int(x) for x in f.read().split('\n') if x]

def find_invalid_number(numbers):
    # test: 5 -- live: 25
    preamble_count = 25
    preamble = numbers[:preamble_count]
    start_value = numbers[preamble_count:]
    while start_value:
        found_value = False
        for i in range(0, preamble_count):
            for j in range(0, preamble_count):
                if i != j:
                    if preamble[i] + preamble[j] == start_value[0]:
                        found_value = True
        if found_value == False:
            return start_value[0]
        preamble.remove(preamble[0])
        preamble.append(start_value[0])
        start_value.remove(start_value[0])
    return None

print(find_invalid_number(numbers))
