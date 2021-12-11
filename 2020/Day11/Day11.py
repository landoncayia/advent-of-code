from copy import deepcopy

num_rows = 97
num_cols = 98


def part1(seats):
    prev_iter = []
    while seats != prev_iter:
        prev_iter = deepcopy(seats)
        for row in range(len(seats)):
            for col in range(len(seats[row])):
                if prev_iter[row][col] == 'L':
                    num_adj = get_num_adj(prev_iter, row, col)
                    if num_adj == 0:
                        seats[row][col] = '#'
                elif prev_iter[row][col] == '#':
                    num_adj = get_num_adj(prev_iter, row, col)
                    if num_adj >= 4:
                        seats[row][col] = 'L'
                elif prev_iter[row][col] == '.':
                    pass
                else:
                    print('unexpected data: closing')
                    exit(1)
    num_occupied = 0
    for row in seats:
        for col in row:
            if col == '#':
                num_occupied += 1
    return num_occupied


def get_num_adj(s, r, c):
    num_adj = 0
    r_lower = max(r-1, 0)
    c_lower = max(c-1, 0)
    r_upper = min(r+1, num_rows-1)
    c_upper = min(c+1, num_cols-1)

    if r_lower != r:
        if s[r_lower][c] == '#':  # adjacent seat up
            num_adj += 1
        if c_lower != c:
            if s[r_lower][c_lower] == '#':  # adjacent seat up-left
                num_adj += 1
        if c_upper != c:
            if s[r_lower][c_upper] == '#':  # adjacent seat up-right
                num_adj += 1
    if r_upper != r:
        if s[r_upper][c] == '#':  # adjacent seat down
            num_adj += 1
        if c_lower != c:
            if s[r_upper][c_lower] == '#':  # adjacent seat down-left
                num_adj += 1
        if c_upper != c:
            if s[r_upper][c_upper] == '#':  # adjacent seat down-right
                num_adj += 1
    if c_lower != c:
        if s[r][c_lower] == '#':  # adjacent seats left
            num_adj += 1
    if c_upper != c:
        if s[r][c_upper] == '#':  # adjacent seats right
            num_adj += 1

    return num_adj


with open('input.txt', 'r') as f:
    seating_data = [list(s.rstrip('\n')) for s in f.readlines()]


occupied = part1(seating_data)
print(occupied)
