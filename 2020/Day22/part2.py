with open('data.txt', 'r') as f:
    data = [x.split('\n')[1:] for x in f.read().split('\n\n') if x]

player_one_data = [int(d) for d in data[0]]
player_two_data = [int(d) for d in data[1]]


class Round:
    def __init__(self):
        self.previous_rounds = {}
        self.current_round = 1


def recursive_combat(deck_one, deck_two, round_info):
    while len(deck_one) > 0 and len(deck_two) > 0:
        if [deck_one, deck_two] in round_info.previous_rounds.values():
            return [deck_one, []]
        round_info.previous_rounds[round_info.current_round] = [deck_one[:], deck_two[:]]
        card_one = deck_one.pop(0)
        card_two = deck_two.pop(0)
        if len(deck_one) >= card_one and len(deck_two) >= card_two:
            new_round = Round()
            new_game = recursive_combat(deck_one[:card_one], deck_two[:card_two], new_round)
            if len(new_game[0]) > len(new_game[1]):
                deck_one += [card_one, card_two]
            else:
                deck_two += [card_two, card_one]
        else:
            if card_one > card_two:
                deck_one += [card_one, card_two]
            else:
                deck_two += [card_two, card_one]
        round_info.current_round += 1
    return [deck_one, deck_two]


start_round = Round()
completed_game = recursive_combat(player_one_data[:], player_two_data[:], start_round)
print(completed_game)

winning_player = completed_game[0] + completed_game[1]
solution = 0
position = 1
for value in reversed(winning_player):
    solution += value * position
    position += 1
print(solution)