with open('data.txt', 'r') as f: answers = f.read().split('\n\n')

cleaned_answers = []
results = []

for x in answers:
    cleaned_answers.append([v for v in x.split('\n') if v])

for group_answers in cleaned_answers:
    group_result = {}
    group_size = len(group_answers)
    collective_yes = 0
    for answers in group_answers:
        for answer in answers:
            if answer in group_result.keys():
                group_result[answer] += 1
            else:
                group_result[answer] = 1
    for key in group_result.keys():
        if group_result[key] == group_size:
            collective_yes += 1
    results.append(collective_yes)
    
print(sum(results))
