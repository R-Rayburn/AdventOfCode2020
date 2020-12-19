with open('data.txt', 'r') as f: fields, my_ticket, nearby_tickets = [x.strip() for x in f.read().split('\n\n') if x]

class Field:
    def __init__(self, field):
        self.name, ranges = field.split(': ')
        range1, range2 = ranges.split(' or ')
        range1 = [int(x) for x in range1.split('-')]
        self.range_one = range(range1[0], range1[1] + 1)
        range2 = [int(x) for x in range2.split('-')]
        self.range_two = range(range2[0], range2[1] + 1)

    def in_range(self, value):
        return value in self.range_one or value in self.range_two

fields = [Field(x) for x in fields.split('\n')]
_, my_ticket = my_ticket.split('\n')
my_ticket = [int(x) for x in my_ticket.split(',')]
nearby_tickets = [ [int(x) for x in ticket.split(',')] for ticket in nearby_tickets.split('\n')[1:] ]
valid_value = {}
invalid_values = []
for i in range(len(nearby_tickets)):
    valid_ticket = True
    valid_value[i] = []
    for value in nearby_tickets[i]:
        value_in_field = []
        for field in fields:
            value_in_field.append(field.in_range(value))
        if value_in_field == [False]*len(fields):
            invalid_values.append(i)
        else:
            valid_value[i].append(value_in_field)

# Remove invalid tickets
invalid_values.reverse()
for v in invalid_values:
    nearby_tickets.pop(v)
    valid_value.pop(v, None)

valid_fields = []
for i in range(len(fields)):
    valid_indices = []
    for j in range(len(fields)):
        indecies = []
        for key in valid_value.keys():
            indecies.append(valid_value[key][i][j])
        valid_indices.append(all(indecies))
    valid_fields.append([index for index in range(len(valid_indices)) if valid_indices[index]])

field_order = {}
while len(field_order.keys()) != len(fields):
    for i in range(len(valid_fields)):
        if len(valid_fields[i]) == 1:
            field_order[i] = valid_fields[i][0]
        elif len(valid_fields[i]) > 1:
            valid_fields[i] = [v for v in valid_fields[i] if v not in field_order.values()]

new_val = 1
for value in field_order.keys():
    if 'departure' in fields[field_order[value]].name:
        new_val *= my_ticket[value]
print(new_val)
