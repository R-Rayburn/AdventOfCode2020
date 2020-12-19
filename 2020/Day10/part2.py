from itertools import groupby

with open('data.txt', 'r') as f: numbers = [int(x) for x in f.read().split('\n') if x]

numbers.append(0)
numbers.sort()

intervals = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]

val = 1
group_counts = [len(g) for g in [list(j) for i, j in groupby(intervals)] if 1 in g]

for i in group_counts:
    if i == 1:
        val *= 1
    if i == 2:
        val *= 2
    if i == 3:
        val *= 4
    if i == 4:
        val *= 7
print(val)
