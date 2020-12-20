import re


def messages_match_regex(reg, msgs):
    match = []
    for m in msgs:
        if re.fullmatch('^{}$'.format(reg), m):
            match.append(m)
    return len(match)


# too low: 389
# too high: 411
with open('data.txt', 'r') as f:
    rules, messages = [x.split('\n') for x in f.read().split('\n\n') if x]

format_rules = {}
for rule in rules:
    index, sub_rule = rule.split(': ')
    if 'a' in sub_rule or 'b' in sub_rule:
        format_rules[index] = sub_rule.replace('"', '')
    else:
        format_rules[index] = sub_rule

format_rules['8'] = ' ( 42 ) + '  # '42 | 42 8'
# Need to figure out aSb Grammar to solve below
# Found in thread where someone mentioned substituting a temp variable
#  and then looping through until no results match.
#  This way I can simulate a^n b^n.
format_rules['11'] = ' ( 42 ) {x} ( 31 ) {x} '  # '42 31 | 42 11 31'

regex = ' ' + format_rules['0'] + ' '
while any(c.isdigit() for c in regex):
    new_regex = regex
    for i in [x for x in re.split('[\\s()|+{}x]', regex[:]) if x]:
        if i in format_rules:
            new_regex = new_regex.replace(' {} '.format(i), ' ( {} ) '.format(format_rules[i]))
    regex = new_regex

valid_regex = 0
count = 1
x = messages_match_regex(regex[:].replace(' ', '').replace('x', str(count)), messages)
while x > 0:
    valid_regex += x
    count += 1
    x = messages_match_regex(regex[:].replace(' ', '').replace('x', str(count)), messages)
print(valid_regex)
