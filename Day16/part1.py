with open('data.txt', 'r') as f: fields, my_ticket, nearby_tickets = [x.strip() for x in f.read().split('\n\n') if x]

class Field:
    def __init__(self, field):
        self.name, ranges = field.split(': ')
        range1, range2 = ranges.split(' or ')
        range1 = [int(x) for x in range1.split('-')]
        self.range_one = range(range1[0], range1[1] + 1)
        range2 = [int(x) for x in range2.split('-')]
        self.range_two = range(range2[0], range2[1] + 1)

fields = [Field(x) for x in fields.split('\n')]
nearby_tickets = [ [int(x) for x in ticket.split(',')] for ticket in nearby_tickets.split('\n')[1:] ]
valid_value = {}
invalid_values = []
for ticket in nearby_tickets:
    valid_ticket = True
    for value in ticket:
        valid_value[value] = []
        value_in_field = []
        for field in fields:
            valid_value[value].append(value in field.range_one or value in field.range_two)
            value_in_field.append(value in field.range_one or value in field.range_two)
        if value_in_field == [False]*len(fields):
            invalid_values.append(value)


false_values = [key for key in valid_value.keys() if valid_value[key] == [False]*len(fields)]
print(invalid_values)
print(sum(invalid_values))
