import copy


acc1 = 0
acc2 = 0


def parse_code(c):
    code_list = []
    for line in c:
        command, value = line.split()
        op = value[0]
        number = int(value[1:])
        code_list.append([command, op, number])
    return code_list


def exec_instr(acc, line, cmd, op, num):
    if cmd == 'acc':
        if op == '+':
            acc += num
            line += 1
            return line, acc
        elif op == '-':
            acc -= num
            line += 1
            return line, acc
    elif cmd == 'jmp':
        if op == '+':
            line += num
            return line, acc
        elif op == '-':
            line -= num
            return line, acc
    elif cmd == 'nop':
        line += 1
        return line, acc


with open('input.txt', 'r') as f:
    data = f.readlines()


def part1(code1):
    global acc1
    reached_lines = []
    curr_line = 0
    next_line = 0
    while curr_line not in reached_lines:
        local_acc1 = 0
        next_line, local_acc1 = exec_instr(local_acc1, curr_line, code1[curr_line][0], code1[curr_line][1],
                                           code1[curr_line][2])
        reached_lines.append(curr_line)
        curr_line = next_line
        acc1 += local_acc1
    return curr_line


def part2(code2):
    found = False
    for i in range(len(code2)-1):
        modified_code2 = copy.deepcopy(code2)
        if modified_code2[i][0] == 'jmp':
            modified_code2[i][0] = 'nop'
            test_instance(modified_code2)
        elif modified_code2[i][0] == 'nop':
            modified_code2[i][0] = 'jmp'
            test_instance(modified_code2)
        elif modified_code2[i][0] == 'acc':
            pass
        if found:
            break


def test_instance(modded):
    global acc2
    reached_lines = []
    local_acc2 = 0
    curr_line = 0
    next_line = 0
    while curr_line != len(modded)-1:
        next_line, local_acc2 = exec_instr(local_acc2, curr_line, modded[curr_line][0], modded[curr_line][1],
                                           modded[curr_line][2])
        reached_lines.append(curr_line)
        curr_line = next_line
        if curr_line in reached_lines:
            return False
    acc2 = local_acc2
    return True


code = parse_code(data)
part1(code)
print(acc1)
part2(code)
print(acc2)
