def main():
    # Part One: 3 right, 1 down
    tree_input = open('input.txt', 'r')
    tree_arr = [x for x in [y for y in tree_input]]
    slope = 3  # right / down = 3 right / 1 down = 3
    count_p1 = count_trees_slope(slope, tree_arr)
    # print(count_p1)

    # Part Two: Other Slopes
    slope_a = 1  # 1 right / 1 down = 1
    # slope = 3 already checked, for 3 right and 1 down; answer was 189
    slope_b = 5  # 5 right / 1 down = 5
    slope_c = 7  # 7 right / 1 down = 7
    slope_d = 0.5  # 1 right / 2 down = 0.5
    count_a = count_trees_slope(slope_a, tree_arr)
    count_b = count_trees_slope(slope_b, tree_arr)
    count_c = count_trees_slope(slope_c, tree_arr)
    count_d = count_trees_slope(slope_d, tree_arr)
    print(f'slope 1: {count_p1}, slope 3: {count_a}, slope 5: {count_b}, slope 7: {count_c}, slope 0.5: {count_d}')
    print(count_p1*count_a*count_b*count_c*count_d)


def count_trees_slope(slope, tree_arr):
    i = 1
    row_length = 31
    tree_count = 0
    for row in tree_arr:
        if i % 1 == 0:
            i = int(i)
            if i % row_length == 0:
                if row[row_length - 1] == '#':
                    tree_count += 1
            else:
                if row[i - 1] == '#':
                    tree_count += 1
        i = (i + slope) % row_length
    return tree_count


if __name__ == '__main__':
    main()
