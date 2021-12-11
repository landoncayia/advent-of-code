def main():
    # Part One: Min and Max Requirements
    password_file = open('input.txt', 'r')
    data = [line.split() for line in password_file]
    password_file.close()
    count_valid = 0
    for item in data:
        # Pre-processing
        min_req, max_req = map(int, item[0].split('-'))
        char = item[1].rstrip(':')
        passwd = item[2]
        # print(min_req, max_req, char, passwd, '\n')
        count = 0
        for i in passwd:
            if i == char:
                count += 1
        if min_req <= count <= max_req:
            count_valid += 1
    print(count_valid)

    print()

    # Part Two: Positions
    count_valid = 0
    for item in data:
        # Pre-processing
        pos_1, pos_2 = map(int, item[0].split('-'))
        char = item[1].rstrip(':')
        passwd = item[2]
        # print(pos_1, pos_2, char, passwd, '\n')
        passwd_as_list = list(passwd)
        if bool(passwd_as_list[pos_1 - 1] == char) ^ bool(passwd_as_list[pos_2 - 1] == char):
            count_valid += 1
    print(count_valid)


if __name__ == '__main__':
    main()
