from collections import deque
with open('data.txt', 'r') as f: rules = f.read().replace('\n', '')

def format_inner_bag(bag):
    amount, adj, color = bag.split(' ')
    return {'amount': int(amount), 'bag': adj + ' ' + color}

def format_inner_bags(bags):
    if 'no other bags' in bags:
        return []
    bags = [x.strip() for x in bags.split(',')]
    bags = [x.replace('bags', '').replace('bag', '').strip() for x in bags]
    bags = [format_inner_bag(x) for x in bags if x]
    return bags

def create_rules(rules):
    rules_graph = {}
    for rule in rules:
        outer_bag, inner_bags = rule.split(' bags contain ')
        inner_bags = format_inner_bags(inner_bags)
        rules_graph[outer_bag] = inner_bags
    return rules_graph

contains_shiny = []
rules = [ r for r in rules.split('.') if r]
searched_bags = []
rules_graph = create_rules(rules)

queue = deque()
queue += ['shiny gold']
while queue:
    bag_to_search = queue.popleft()
    for key in rules_graph.keys():
        if key not in searched_bags:
            ib = [x['bag'] for x in rules_graph[key]]
            if bag_to_search in ib:        
                contains_shiny.append(key)
                searched_bags.append(key)
                queue += [key]

print(len(contains_shiny))
