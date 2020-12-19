#import os
#import glob
#from PIL import Image, ImageDraw
with open('data.txt', 'r') as f: prior_seats = [x for x in f.read().split('\n') if x]

new_seats = prior_seats[:]

def check_for_fill(grid, row, col, row_diff, col_diff):
    if len(grid) <= row or row < 0:
        return 0
    if len(grid[row]) <= col or col < 0:
        return 0
    if grid[row][col] == '#':
        return 1
    if grid[row][col] == 'L':
        return 0
    return check_for_fill(grid, row + row_diff, col + col_diff, row_diff, col_diff)

chaos = True
#inc = 0
while chaos:
    for i in range(len(prior_seats)):
        for j in range(len(prior_seats[i])):
            adj_seats_filled = 0
            if i == 0:
                if j == 0:
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j, 1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j + 1, 1, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1, 0, 1)
                elif j == len(prior_seats[i]) - 1:
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j, 1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1, 0, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j - 1, 1, -1)
                else:
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j, 1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j + 1, 1, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1, 0, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1, 0, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j - 1, 1, -1)
            elif i == len(prior_seats) - 1:
                if j == 0:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1 , j, -1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j + 1, -1, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1, 0, 1)
                elif j == len(prior_seats[i]) - 1:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j, -1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j - 1, -1, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1, 0, -1)
                else:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j, -1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j - 1, -1, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j + 1, -1, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1, 0, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1, 0, 1)
            else:
                if j == 0:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1 , j, -1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j + 1, -1, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1, 0, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j, 1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j + 1, 1, 1)
                elif j == len(prior_seats[i]) - 1:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j, -1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j - 1, -1, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1, 0, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j - 1, 1, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j, 1, 0)
                else:
                    adj_seats_filled += check_for_fill(prior_seats, i - 1 , j, -1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j + 1, -1, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j + 1, 0, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j, 1, 0)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j + 1, 1, 1)
                    adj_seats_filled += check_for_fill(prior_seats, i + 1, j - 1, 1, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i - 1, j - 1, -1, -1)
                    adj_seats_filled += check_for_fill(prior_seats, i, j - 1, 0, -1)
                
            if prior_seats[i][j] == '#' and adj_seats_filled >= 5:
                new_seats[i] = new_seats[i][:j] + 'L' + new_seats[i][j+1:]
            elif prior_seats[i][j] == 'L' and adj_seats_filled == 0:
                new_seats[i] = new_seats[i][:j] + '#' + new_seats[i][j+1:]
            else:
                new_seats[i] = new_seats[i][:j] + prior_seats[i][j] + new_seats[i][j+1:]
    #img = Image.new('RGB', (700,1600), color=(255,255,255))
    #d = ImageDraw.Draw(img)
    #d.text((20, 20), '\n'.join(n for n in new_seats), fill=(0,0,0))
    #img.save('text_' + str(inc) + '.png')
    chaos = prior_seats[:] != new_seats[:]
    temp = prior_seats[:]
    prior_seats = new_seats[:]
    new_seats = temp[:]
    #inc += 1

num_of_seats = 0
for i in prior_seats:
    for j in i:
        if j == '#':
            num_of_seats += 1
print(num_of_seats)


#gif_name = 'day_11'
#file_list = glob.glob('*.png')
#list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0]))

#with open('image_list.txt', 'w') as file:
#    for item in file_list:
#        file.write('%s\n' % item)
#os.system('convert @image_list.txt {}.gif'.format(gif_name))
