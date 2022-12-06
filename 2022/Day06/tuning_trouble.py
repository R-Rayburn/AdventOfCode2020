with open('data.txt', 'r') as file:
    signal_data = file.read()

test_1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
test_2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
test_3 = 'nppdvjthqldpwncqszvftbrmjlhg'
test_4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test_5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'


def find_signal_marker(signal, char_count):
    for i in range(0, len(signal)-char_count-1):
        marker = signal[i:i+char_count]
        duplicats = list(filter(lambda x: marker.count(x) > 1, marker))
        if len(duplicats) == 0:
            return marker
        
    return None


def find_index(signal, char_count=4):
    marker = find_signal_marker(signal, char_count)
    return signal.index(marker) + len(marker)


print('Tuning Trouble')
print('  Part 1')
print(f'    Test 1: {find_index(test_1)}')
print(f'    Test 2: {find_index(test_2)}')
print(f'    Test 3: {find_index(test_3)}')
print(f'    Test 4: {find_index(test_4)}')
print(f'    Test 5: {find_index(test_5)}')
print(f'    Data: {find_index(signal_data)}')
print('  Part 2')
print(f'    Test 1: {find_index(test_1, 14)}')
print(f'    Test 2: {find_index(test_2, 14)}')
print(f'    Test 3: {find_index(test_3, 14)}')
print(f'    Test 4: {find_index(test_4, 14)}')
print(f'    Test 5: {find_index(test_5, 14)}')
print(f'    Data: {find_index(signal_data, 14)}')
