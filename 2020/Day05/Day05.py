with open('input.txt', 'r') as f:
    boarding_passes = f.read().split('\n')


def get_all_ids(passes):
    seat_ids = []
    for bp in passes:
        row_min, row_max = 0, 127
        col_min, col_max = 0, 7
        final_row, final_col = 0, 0
        for c in bp[:6]:
            if c == 'F':
                row_max -= ((row_max - row_min) // 2) + 1
            elif c == 'B':
                row_min += ((row_max - row_min) // 2) + 1
        if bp[6] == 'F':
            final_row = row_min
        elif bp[6] == 'B':
            final_row = row_max
        for c in bp[7:9]:
            if c == 'L':
                col_max -= ((col_max - col_min) // 2) + 1
            elif c == 'R':
                col_min += ((col_max - col_min) // 2) + 1
        if bp[9] == 'L':
            final_col = col_min
        elif bp[9] == 'R':
            final_col = col_max
        # print(row_min, row_max, col_min, col_max)
        seat_ids.append(final_row * 8 + final_col)
    return seat_ids


# Part One: Highest Seat ID
all_seats = get_all_ids(boarding_passes)

max_seat_id = max(all_seats)

print(max_seat_id)

# Part Two: Where is your seat?
ans = [seat for seat in range(min(all_seats), max(all_seats)) if seat not in all_seats]
print(ans[0])
