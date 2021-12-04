print('Not Quite Lisp')

data = open('data.txt', 'r').read()


def find_floor(d):
    floor = 0
    for p in d:
        if p == '(':
            floor += 1
        else:
            floor -= 1
    return floor


print('Part 1')
print(f'Test 1: {find_floor("(())")}')  # 0
print(f'Test 2: {find_floor("()()")}')  # 0
print(f'Test 3: {find_floor("(((")}')  # 3
print(f'Test 4: {find_floor("(()(()(")}')  # 3
print(f'Test 5: {find_floor("))(((((")}')  # 3
print(f'Test 6: {find_floor("())")}')  # -1
print(f'Test 7: {find_floor("))(")}')  # -1
print(f'Test 8: {find_floor(")))")}')  # -3
print(f'Test 9: {find_floor(")())())")}')  # -3
print(f'Data: {find_floor(data)}')


def find_position_that_leads_to_basement(directions):
    floor = 0
    position = 0
    for d in directions:
        if d == '(':
            floor += 1
        else:
            floor -= 1
        position += 1
        if floor < 0:
            return position
    return None


print('Part 2')
print(f'Test 1: {find_position_that_leads_to_basement(")")}')  # 1
print(f'Test 2: {find_position_that_leads_to_basement("()())")}')  # 5
print(f'Data: {find_position_that_leads_to_basement(data)}')
