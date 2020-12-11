with open('data.txt', 'r') as f: prior_seats = [x for x in f.read().split('\n') if x]

new_seats = prior_seats[:]

def check_for_fill(grid, row, col):
    if grid[row][col] == '#':
        return 1
    return 0

chaos = True

while chaos:
    for i in range(len(prior_seats)):
        for j in range(len(prior_seats[i])):
            adj_seats_filled = 0
            if i == 0:
                if j == 0:
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1)
                elif j == len(prior_seats[i]) - 1:
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j - 1)
                else:
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j - 1)
            elif i == len(prior_seats) - 1:
                if j == 0:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1 , j)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1)
                elif j == len(prior_seats[i]) - 1:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1)
                else:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1)
            else:
                if j == 0:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1 , j)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j)
		    adj_seats_filled += check_for_fill(prior_seats, i + 1, j + 1)
                elif j == len(prior_seats[i]) - 1:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j)
		    adj_seats_filled += check_for_fill(prior_seats, i - 1, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j)
                else:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1 , j)
		    adj_seats_filled += check_for_fill(prior_seats, i - 1, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j)
		    adj_seats_filled += check_for_fill(prior_seats, i + 1, j + 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j - 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1)
                
            if prior_seats[i][j] == '#' and adj_seats_filled >= 4:
                new_seats[i] = new_seats[i][:j] + 'L' + new_seats[i][j+1:]
            elif prior_seats[i][j] == 'L' and adj_seats_filled == 0:
                new_seats[i] = new_seats[i][:j] + '#' + new_seats[i][j+1:]
            else:
                new_seats[i] = new_seats[i][:j] + prior_seats[i][j] + new_seats[i][j+1:]
    chaos = prior_seats[:] != new_seats[:]
    temp = prior_seats[:]
    prior_seats = new_seats[:]
    new_seats = temp[:]

num_of_seats = 0
for i in prior_seats:
    for j in i:
        if j == '#':
            num_of_seats += 1
print(num_of_seats)
