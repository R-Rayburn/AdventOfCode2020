"""Calorie Counting"""
print('Calorie Counting')

with open('data.txt', 'r', encoding='UTF-8') as data:
    data_calories = [
        sum(c) for c in [
            [int(a) for a in x.split('\n')] for x in data.read().split('\n\n') if x
        ]
    ]
with open('test.txt', 'r', encoding='UTF-8') as test:
    test_calories = [
        sum(c) for c in [
            [int(a) for a in x.split('\n')] for x in test.read().split('\n\n') if x
        ]
    ]

print('Part 1')
print(f'Test: {max(test_calories)}')
print(f'Data: {max(data_calories)}')

print('Part 2')
print(f'Test: {sum(sorted(test_calories, reverse=True)[:3])}')
print(f'Data: {sum(sorted(data_calories, reverse=True)[:3])}')
