with open('data.txt', 'r') as f: answers = f.read().split('\n\n')

cleaned_answers = []
results = []

for x in answers:
    cleaned_answers.append([v for v in x.split('\n') if v])

for group_answers in cleaned_answers:
    group_result = set()
    for answers in group_answers:
        for answer in answers:
            group_result.add(answer)
    results.append(len(group_result))
    
print(sum(results))
