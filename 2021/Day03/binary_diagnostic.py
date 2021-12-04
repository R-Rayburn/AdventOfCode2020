print('Binary Diagnostic')

with open('data.txt', 'r') as data:
    diagnostic_report = [x for x in data.read().split('\n') if x]
with open('test.txt', 'r') as test:
    test_report = [x for x in test.read().split('\n') if x]


def inverse_binary(binary):
    return ''.join(['1' if b == '0' else '0' for b in binary])


def find_gamma_rate(report):
    gamma_rate = ''
    for i in range(len(report[0])):
        bin_count = {'0': 0, '1': 0}
        for r in report:
            bin_count[r[i]] += 1
        new_bit = max(bin_count, key=bin_count.get)
        gamma_rate += new_bit
    return gamma_rate


def find_epsilon_rate(gamma_rate):
    return inverse_binary(gamma_rate)


def find_power_consumption(report):
    gamma_rate = find_gamma_rate(report)
    epsilon_rate = find_epsilon_rate(gamma_rate)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


print('Part 1')
print(f'Test: {find_power_consumption(test_report)}')
print(f'Data: {find_power_consumption(diagnostic_report)}')


def get_new_report(index, bit, report):
    return [x for x in report if x[index] == bit]


def find_oxygen_generator_rating(index, report):
    if len(report) == 1:
        return report[0]
    bin_count = {'0': 0, '1': 0}
    for r in report:
        bin_count[r[index]] += 1
    max_bit = '0' if bin_count['1'] < bin_count['0'] else '1'
    new_report = get_new_report(index, max_bit, report)
    return find_oxygen_generator_rating(index + 1, new_report)


def find_co2_scrubber_rating(index, report):
    if len(report) == 1:
        return report[0]
    bin_count = {'0': 0, '1': 0}
    for r in report:
        bin_count[r[index]] += 1
    min_bit = '1' if bin_count['1'] < bin_count['0'] else '0'
    new_report = get_new_report(index, min_bit, report)
    return find_co2_scrubber_rating(index+1, new_report)


def find_life_support_rating(report):
    oxygen_generator_rating = find_oxygen_generator_rating(0, report)
    co2_scrubber = find_co2_scrubber_rating(0, report)
    return int(oxygen_generator_rating, 2) * int(co2_scrubber, 2)


print('Part 2')
print(f'Test: {find_life_support_rating(test_report)}')
print(f'Data: {find_life_support_rating(diagnostic_report)}')
