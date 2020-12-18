import math as m

with open('data.txt', 'r') as f: seat_locations = f.read()

seat_locations = [sl for sl in seat_locations.split('\n') if sl]

row_min = 0
row_max = 127
col_min = 0
col_max = 7

highest_id = 0

def calculate_seat_id(row, col):
    return row * 8 + col

def calculate_middle(lower, upper):
    return (upper + lower) / 2

def find_row(lower, upper, val):
    if val == 'F':
        return lower
    elif val == 'B':
        return upper
    elif val[:1] == 'F':
        return find_row(lower, m.floor(calculate_middle(lower, upper)), val[1:])
    else:
        return find_row(m.ceil(calculate_middle(lower, upper)), upper, val[1:])

def find_col(lower, upper, val):
    if val == 'R':
        return upper
    elif val == 'L':
        return lower
    elif val[:1] == 'R':
        return find_col(m.ceil(calculate_middle(lower, upper)), upper, val[1:])
    else:
        return find_col(lower, m.floor(calculate_middle(lower, upper)), val[1:])

for seat_loc in seat_locations:
    row = find_row(row_min, row_max, seat_loc[:7])
    col = find_col(col_min, col_max, seat_loc[7:])
    seat_id = calculate_seat_id(row, col)
    print(seat_id)
    if seat_id > highest_id:
        highest_id = seat_id

print(highest_id)
