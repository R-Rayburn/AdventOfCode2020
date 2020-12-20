import re

with open('data.txt', 'r') as f:
    rules, messages = [x.split('\n') for x in f.read().split('\n\n') if x]

format_rules = {}
for rule in rules:
    index, sub_rule = rule.split(': ')
    if 'a' in sub_rule or 'b' in sub_rule:
        format_rules[index] = sub_rule.replace('"', '')
    else:
        format_rules[index] = sub_rule

regex = ' ' + format_rules['0'] + ' '
while any(c.isdigit() for c in regex):
    new_regex = regex
    print(regex)
    for i in [x for x in re.split('[\\s()|^$]', regex[:]) if x]:
        if i in format_rules:
            # print(' {} '.format(i))
            # print(' ({}) '.format(format_rules[i]))
            new_regex = new_regex.replace(' {} '.format(i), ' ( {} ) '.format(format_rules[i]))
    regex = new_regex

count = 0
for message in messages:
    if re.fullmatch('^{}$'.format(regex.replace(' ', '')), message):
        count += 1
        print(message)
print(count)