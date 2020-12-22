with open('data.txt', 'r') as f:
    data = [x.split('\n')[1:] for x in f.read().split('\n\n') if x]

player_one_data = [int(d) for d in data[0]]
player_two_data = [int(d) for d in data[1]]

while len(player_one_data) > 0 and len(player_two_data) > 0:
    p1_card = player_one_data.pop(0)
    p2_card = player_two_data.pop(0)
    if p1_card > p2_card:
        player_one_data += [p1_card, p2_card]
    else:
        player_two_data += [p2_card, p1_card]

winning_player = player_two_data + player_one_data
solution = 0
position = 1
for value in reversed(winning_player):
    solution += value * position
    position += 1
print(solution)