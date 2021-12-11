def main():
    # Part One: 2 NUMBERS
    expenses_file = open('input.txt', 'r')
    expenses = [int(exp) for exp in expenses_file]
    expenses_file.close()
    for exp_i in expenses:
        exp_j = 2020 - exp_i
        if exp_j in expenses:
            print(exp_i * exp_j)
            break

    print()

    # Part Two: 3 NUMBERS
    for i in range(len(expenses)):
        for j in range(i+1, len(expenses)):
            exp_i = expenses[i]
            exp_j = expenses[j]
            exp_k = 2020 - exp_i - exp_j
            if exp_k in expenses:
                print(exp_i * exp_j * exp_k)
                break


if __name__ == '__main__':
    main()
