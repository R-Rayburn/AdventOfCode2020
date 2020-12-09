from collections import deque
with open('data.txt', 'r') as f: rules = f.read().replace('\n', '')

def format_inner_bag(bag):
    amount, adj, color = bag.split(' ')
    return (adj + ' ' + color, int(amount))
    
def format_inner_bags(bags):
    if 'no other bags' in bags:
        return {}
    bags = [x.strip() for x in bags.split(',')]
    bags = [x.replace('bags', '').replace('bag', '').strip() for x in bags]
    formatted_bags = {}
    for bag in bags:
        if bag:
            color, amount = format_inner_bag(bag)
            formatted_bags[color] = amount
    return formatted_bags

def create_rules(rules):
    rules_graph = {}
    for rule in rules:
        outer_bag, inner_bags = rule.split(' bags contain ')
        inner_bags = format_inner_bags(inner_bags)
        rules_graph[outer_bag] = inner_bags
    return rules_graph

def find_prod(inner, outer, graph):
    prod = 0
    if len(inner) == 0:
        return 0
    else:
        for i in inner:
            prod += graph[outer][i] + (graph[outer][i] * find_prod(graph[i].keys() ,i, graph))
    return prod

rules = [ r for r in rules.split('.') if r]
rules_graph = create_rules(rules)
bag_to_search = 'shiny gold'
inner_bags = rules_graph[bag_to_search].keys()
total_inner_bags = find_prod(inner_bags, bag_to_search, rules_graph)

print(total_inner_bags)
